import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def send_report_email(sender_email, app_password, receiver_email, report_path):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = f"Daily Scraping Report - {datetime.now().strftime('%Y-%m-%d')}"
    
    body = f"""
Hello!

Your automated scraping report is ready.

Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Please find the attached Excel report with all the data.

Best regards,
Your Automation Bot
    """
    msg.attach(MIMEText(body, "plain"))
    
    with open(report_path, "rb") as file:
        attachment = MIMEApplication(file.read(), Name="scraping_report.xlsx")
        attachment["Content-Disposition"] = f'attachment; filename="scraping_report.xlsx"'
        msg.attach(attachment)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        logging.info("✅ Report emailed successfully!")
    except Exception as e:
        logging.error(f"❌ Failed: {e}")

# Apna ecommerce bot ka Excel report bhejo
send_report_email(
    sender_email="YOUR_EMAIL_HERE",
    app_password="YOUR_APP_PASSWORD_HERE",
    receiver_email="YOUR_EMAIL_HERE",
    report_path="C:/projects/ecommerce_bot/output/books_report.xlsx"
)