# https://codewithmosh.com/courses/417695/lectures/8417583

# Multi-purpose Internet Mail Extensions
# Multipart is HTML and plain text
from email.mime.multipart import MIMEMultipart
# Import MIMEText to attach the body
from email.mime.text import MIMEText
# To attache images
from email.mime.image import MIMEImage
# To import image from path
from pathlib import Path


# For the SMTP
import smtplib


message = MIMEMultipart()
message["from"] = "Brendan Ring"
message["to"] = "user@test.com"
message["subject"] = "This is a test"
# Attach the body
message.attach(MIMEText("Body"))
# Attache an image passed as binary
message.attach(MIMEImage(Path("test.png").read_bytes()))

# Send message using the SMTP server
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # follow smtp protocol with hello message
    smtp.ehlo()
    # start tls encryption
    smtp.starttls
    smtp.login("testuser@test.com", "password")
    smtp.send_message(message)
    print("Sent...")
