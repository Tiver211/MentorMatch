import os
import smtplib
from email.mime.text import MIMEText

SMTP_HOST = "postfix"
SMTP_PORT = 1025
SMTP_USER = "noreply@prod-team-35-lg7sic6v.final.prodcontest.ru"
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

def send_email(target: str, title: str, body: str):
    msg = MIMEText(body)
    msg['Subject'] = title
    msg['From'] = SMTP_USER
    msg['To'] = target

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, [target], msg.as_string())
