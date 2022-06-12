import os
import smtplib
from email.message import EmailMessage


class SendMessageFromEmail:
    def __init__(self, sender_email, sender_email_password):
        self.sender = sender_email
        self.password = sender_email_password
        self.port = os.environ.get('PORT')
        self.server = os.environ.get('SERVER')

    def send_message(self, receiver: str, subject: str, message: str) -> None:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = receiver
        msg.set_content(message)

        with smtplib.SMTP_SSL(self.server, int(self.port)) as smtp:
            aa = smtp.login(self.sender, self.password)
            print(aa)
            smtp.send_message(msg)


Email = SendMessageFromEmail(
    sender_email=os.environ.get("EMAIL"),
    sender_email_password=os.environ.get("EMAIL_PASSWORD")
)

Email.send_message(
    receiver="RECEIVER EMAIL PASTE HERE",
    subject="Simple email from python",
    message="This message sended by python code. Example email to demonstrate"
)
