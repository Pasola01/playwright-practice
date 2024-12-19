import imaplib
import time
import sys
import mailparser
import email
import email.header
from mailparser import MailParser
from bs4 import BeautifulSoup


class MailReadService:
    """Service for finding email from autto on User Email"""

    def __init__(self, user_email: str, user_password: str) -> None:
        self.email_account = user_email
        self.email_pass = user_password
        self.im = imaplib.IMAP4_SSL("imap.gmail.com")

    def find_email(self, email_type: str, **kwargs) -> str:
        """Find email by type.

        :param email_type: email type which need to find. available ->
                           registration, invitation, export_success, export_error
        :param kwargs: imported file name
        """

        imported_file_name = kwargs.get("imported_file_name", "")
        delete_after_reading = kwargs.get("delete_after_reading", False)

        try:
            result = None
            self.im.login(self.email_account, self.email_pass)

            try_times = 60

            while try_times > 0 and not result:
                time.sleep(5)
                try_times -= 1

                rv, data = self.im.select()

                if rv == "OK":
                    if email_type == "registration":
                        result = self._find_registration_email()
                    elif email_type == "invitation":
                        result = self._find_invitation_email(delete_after_reading=delete_after_reading)
                    elif email_type == "export_success":
                        result = self._find_export_email(email_type, imported_file_name)
                    elif email_type == "export_error":
                        result = self._find_export_email(email_type, imported_file_name)
                else:
                    print("ERROR: Unable to open mailbox ", rv)

                self.im.close()

            self.im.logout()

            return result

        except imaplib.IMAP4.error as e:
            print(f"LOGIN FAILED!!! {str(e)}")
            sys.exit(1)

    def find_email_by_subject(self, email_subject: str, body_text=None, **kwargs) -> MailParser:
        try:
            result = None
            self.im.login(self.email_account, self.email_pass)

            try_times = 240

            while try_times > 0 and not result:
                time.sleep(5)
                try_times -= 1

                rv, data = self.im.select()

                if rv == "OK":
                    rv, data = self.im.search(None, f'To "{self.email_account}" SUBJECT "{email_subject}"')
                    if rv != "OK" or not data[0]:
                        print("No messages found!")
                        continue

                    mail_list = data[0].decode("utf-8").split()
                    for m in reversed(mail_list):
                        rv, data = self.im.fetch(m, "(RFC822)")
                        tmp_result = mailparser.parse_from_bytes(data[0][1])
                        if kwargs.get("delete_after_reading", False) == "True":
                            self.im.store(m, "+FLAGS", "\\Deleted")

                        if body_text:
                            used_link_result = True
                            if used_resume_links := body_text.get("used_resume_links"):
                                for i in used_resume_links:
                                    if i in tmp_result.body:
                                        used_link_result = False
                            if session_id := body_text.get("session_id"):
                                if session_id in tmp_result.body and used_link_result:
                                    result = tmp_result
                                    break
                        else:
                            result = tmp_result
                            break
                else:
                    print("ERROR: Unable to open mailbox ", rv)

            self.im.close()
            self.im.logout()

            if not result:
                raise Exception(f"Email with '{email_subject}' subject was not found!")

            return result

        except imaplib.IMAP4.error as e:
            print(f"LOGIN FAILED!!! {str(e)}")
            sys.exit(1)

    def _find_registration_email(self) -> str | None:
        """
        Find registration email
        """

        rv, data = self.im.search(None, f"(To '{self.email_account}')")
        if rv != "OK":
            print("No messages found!")
            return

        for num in data[0].split():
            rv, data = self.im.fetch(num, "(RFC822)")
            if rv != "OK":
                print("ERROR getting message", num)
                return

            msg = email.message_from_bytes(data[0][1])
            to = str(email.header.make_header(email.header.decode_header(msg["To"])))  # noqa

            soup = BeautifulSoup(msg.get_payload(decode=True), "html.parser")
            activation_link = soup.find_all("a")[1].get("href")

            return activation_link

    def _find_invitation_email(self, **kwargs) -> str | None:
        """
        Find invitation email
        """

        rv, data = self.im.search(None, f"(To '{self.email_account}')")
        if rv != "OK":
            print("No messages found!")
            return

        for num in data[0].split():
            rv, data = self.im.fetch(num, "(RFC822)")
            if rv != "OK":
                print("ERROR getting message", num)
                return

            msg = email.message_from_bytes(data[0][1])

            soup = BeautifulSoup(msg.get_payload(decode=True), "html.parser")
            activation_link = soup.find_all("a")[0].get("href")

            if kwargs.get("delete_after_reading", False) == "True":
                self.im.store(num, "+FLAGS", "\\Deleted")

            return activation_link

    def _find_export_email(self, export_type, imported_file_name) -> str | None:
        """Find export message"""

        if export_type == "export_error":
            subject = "Autto Data Table Import Errors"
        elif export_type == "export_success":
            subject = "Autto Data Table Import Successful"
        else:
            raise Exception(f"export type: {export_type} - is not supported in _find_export_email func.")

        rv, data = self.im.search(None, f'To "{self.email_account}" SUBJECT "{subject}" TEXT "{imported_file_name}"')
        if rv != "OK":
            print("No messages found!")
            return

        for num in data[0].split():
            rv, data = self.im.fetch(num, "(RFC822)")
            if rv != "OK":
                print("ERROR getting message", num)
                return

            msg = email.message_from_bytes(data[0][1])

            soup = BeautifulSoup(msg.get_payload(decode=True), "html.parser")
            email_body = soup.find("p").text

            return email_body
