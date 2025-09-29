import smtplib, os
from email.mime.text import MIMEText
from twilio.rest import Client

def send_alerts(results):
    if not results:
        return
    message = "Breakout alerts:\n" + "\n".join([r["ticker"] for r in results])
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")
    recipient = os.getenv("ALERT_EMAIL")
    if smtp_server and smtp_user and smtp_pass and recipient:
        msg = MIMEText(message)
        msg["Subject"] = "Breakout Alerts"
        msg["From"] = smtp_user
        msg["To"] = recipient
        with smtplib.SMTP_SSL(smtp_server, 465) as server:
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, recipient, msg.as_string())
    tw_sid = os.getenv("TWILIO_SID")
    tw_token = os.getenv("TWILIO_TOKEN")
    tw_from = os.getenv("TWILIO_FROM")
    tw_to = os.getenv("ALERT_PHONE")
    if tw_sid and tw_token and tw_from and tw_to:
        client = Client(tw_sid, tw_token)
        client.messages.create(body=message, from_=tw_from, to=tw_to)
