import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

import openai 

openai.api_key = '[insert the API key]'

messages = [{"role": "system", "content": "write me a story using the following phrase: Valentine's Day Hackathon"}]


chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)
reply = chat.choices[0].message.content


def send_email():
    # Email configuration
    sender_email = "thestorycreator12@gmail.com"
    receiver_email = "maxeng017@gmail.com"
    subject = "Daily Story"
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    # Email body
    body = reply
    msg.attach(MIMEText(body, 'plain'))
    # SMTP server configuration (for Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "thestorycreator12@gmail.com"
    smtp_password = "insert password"
    # Establish a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    # Log in to the email account
    server.login(smtp_username, smtp_password)
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    # Quit the server
    server.quit()
# Schedule the script to run daily at a specific time (adjust as needed)
schedule.every().day.at("19:00").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
