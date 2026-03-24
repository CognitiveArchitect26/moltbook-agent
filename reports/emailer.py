import os
import smtplib
from email.message import EmailMessage


def send_email_report(subject, body, to_email):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    if not sender_email or not sender_password:
        raise ValueError("Missing SENDER_EMAIL or SENDER_PASSWORD in environment variables.")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.mail.me.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    return f"Email sent to {to_email}"