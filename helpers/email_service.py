import imaplib
import email
import re
from email.header import decode_header


class GmailReader:
    def __init__(self, email_user: str, app_password: str) -> None:
        """
        Ініціалізація з даними для доступу до Gmail.
        :param email_user: Електронна адреса користувача.
        :param app_password: Пароль додатку для доступу до Gmail.
        """
        self.email_user = email_user
        self.app_password = app_password
        self.mail = None

    def connect(self) -> None:
        """Підключення до сервера IMAP Gmail."""
        self.mail = imaplib.IMAP4_SSL("imap.gmail.com")
        self.mail.login(self.email_user, self.app_password)

    def disconnect(self) -> None:
        """Закриття з'єднання з сервером."""
        if self.mail:
            self.mail.close()
            self.mail.logout()

    def get_otp(self) -> str | None:
        """Отримання OTP із останнього листа."""
        # Вибираємо папку "INBOX"
        self.mail.select("inbox")

        # Шукаємо останній лист
        status, messages = self.mail.search(None, 'ALL')
        mail_ids = messages[0].split()

        # Отримуємо ID останнього листа
        latest_email_id = mail_ids[-1]

        # Отримуємо дані останнього листа
        status, msg_data = self.mail.fetch(latest_email_id, "(RFC822)")

        # Парсимо лист
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # Декодуємо тему (Subject) для перевірки наявності OTP
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")

                # Перевіряємо, чи є в темі листа OTP
                if "Your OTP Code" in subject:
                    # Якщо лист має частини (наприклад, текст і HTML), розбираємо тільки текст
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            # Перевіряємо, чи це текстова частина
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                otp_text = part.get_payload(decode=True).decode()
                                break
                    else:
                        # Якщо лист не мультимедійний
                        otp_text = msg.get_payload(decode=True).decode()

                    # Використовуємо регулярний вираз для пошуку OTP (залежно від формату коду)
                    otp_code = re.search(r'\b\d{6}\b', otp_text)  # Приклад для 6-значного OTP
                    if otp_code:
                        return otp_code.group()

        return None


    def get_forgot_password_link(self):
        """Отримання посилання для відновлення пароля з останнього листа."""
        self.mail.select("inbox")

        # Шукаємо останній лист
        status, messages = self.mail.search(None, 'ALL')
        mail_ids = messages[0].split()
        latest_email_id = mail_ids[-1]

        # Отримуємо дані останнього листа
        status, msg_data = self.mail.fetch(latest_email_id, "(RFC822)")

        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            email_text = part.get_payload(decode=True).decode()
                            break
                else:
                    email_text = msg.get_payload(decode=True).decode()

                # Використовуємо регулярний вираз для пошуку посилання
                password_link = re.search(r'https://practice\.expandtesting\.com/\S+', email_text)
                if password_link:
                    return password_link.group()
        return None

