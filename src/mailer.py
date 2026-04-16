"""Gmail SMTP によるメール送信."""

import smtplib
from email.mime.text import MIMEText


def send_mail(
    gmail_address: str,
    app_password: str,
    to_address: str,
    subject: str,
    body: str,
) -> None:
    """Gmail の SMTP 経由でメールを送信する.

    Args:
        gmail_address: 送信元 Gmail アドレス
        app_password: Gmail アプリパスワード (16文字)
        to_address: 送信先メールアドレス
        subject: 件名
        body: 本文
    """
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = gmail_address
    msg["To"] = to_address

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as smtp:
        smtp.starttls()
        smtp.login(gmail_address, app_password)
        smtp.send_message(msg)
