import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import time

# Load the recipient list
data = pd.read_excel('recipients.xlsx')  # Ensure the file has columns: Name, Email, Message
email_list = data.to_dict(orient='records')

# SMTP Server Configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_email@gmail.com"
sender_password = "your_password"

# Function to send email
def send_email(to_email, subject, body, attachment_path=None):
    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject

        # Add email body
        message.attach(MIMEText(body, 'plain'))

        # Add attachment if specified
        if attachment_path:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
            message.attach(part)

        # Send the email
        server.send_message(message)
        print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

# Connect to the SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    print("Successfully connected to the SMTP server.")

    # Loop through recipients and send emails
    for recipient in email_list:
        name = recipient['Name']
        to_email = recipient['Email']
        custom_message = recipient.get('Message', f"Hello {name},\n\nThis is a test email.")
        subject = "Your Custom Subject Here"

        # Example of adding an attachment (set to None if not needed)
        attachment = None  # Replace with a valid file path if needed

        # Send the email
        send_email(to_email, subject, custom_message, attachment)

        # Delay to prevent being flagged as spam
        time.sleep(2)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Disconnect from the server
    server.quit()
    print("Disconnected from the SMTP server.")
