import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "postfix"
port = 25
login = "MFS"
password = os.getenv("SMTP_PASSWORD")  # Пароль для SMTP


def send_email(target, subject, content):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = "noreply@prod-team-35-lg7sic6v.final.prodcontest.ru"
    message["To"] = target
    text = MIMEText(content)
    message.attach(text)

    with smtplib.SMTP(smtp_server, port) as server:
        server.sendmail("noreply@prod-team-35-lg7sic6v.final.prodcontest.ru", target, message.as_string())