import smtplib, ssl
from constants import username, password
from email.message import EmailMessage


def send_email(sender, message):
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()
    receiver = username

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        msg = EmailMessage()
        msg['From'] = sender
        msg['To'] = username
        msg['Subject'] = "Email inquiry from: " + sender
        msg.set_content(message + "\nSender: " + sender)
        server.send_message(msg)

if __name__ == '__main__':
    send_email()