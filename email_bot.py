import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def send_email(sender_email, app_password, receiver_email, subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    
    msg.attach(MIMEText(body, "plain"))
    
    if attachment_path:
        with open(attachment_path, "rb") as file:
            attachment = MIMEApplication(file.read(), Name="report.xlsx")
            attachment["Content-Disposition"] = f'attachment; filename="report.xlsx"'
            msg.attach(attachment)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

send_email(
    sender_email="YOUR_EMAIL_HERE",
    app_password="YOUR_APP_PASSWORD_HERE",
    receiver_email="YOUR_EMAIL_HERE",
    subject="Test Email from Python Bot",
    body="Hello! This is an automatic email from my Python bot."
)