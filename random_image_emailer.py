import smtplib
from email.message import EmailMessage
import schedule
import time
import os
import random
import logging
import imagesize
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Send emails with a random image attachment.')
parser.add_argument('--sender-email', required=True, help='Sender email address')
parser.add_argument('--recipient-email', required=True, help='Recipient email address')
parser.add_argument('--smtp-server', required=True, help='SMTP server address')
parser.add_argument('--smtp-port', type=int, required=True, help='SMTP server port')
parser.add_argument('--smtp-user-name', required=True, help='SMTP server username')
parser.add_argument('--smtp-password', required=True, help='SMTP server password')
parser.add_argument('--image-dir', required=True, help='Directory where images are stored')
parser.add_argument('--schedule', required=True, help='The time the email should be sent each day in HH:MM format.')
parser.add_argument('--debug', required=True, help='Whether debugging mode is on. Will send out test email immediately.')

args = parser.parse_args()

def get_mime_type(file_extension):
    """Simple function to guess MIME type based on file extension."""
    if file_extension.lower() in ['.jpg', '.jpeg']:
        return 'jpeg'
    elif file_extension.lower() == '.png':
        return 'png'
    elif file_extension.lower() == '.gif':
        return 'gif'
    else:
        return 'octet-stream'  # Default binary type

def send_email_with_image():
    logging.info("Attempting to send an email with a random image...")
    
    try:
        image_path = random.choice(os.listdir(args.image_dir))
        full_image_path = os.path.join(args.image_dir, image_path)
        width, height = imagesize.get(full_image_path)
        logging.info(f"Selected image: {image_path} with dimensions {width}x{height}")
    except Exception as e:
        logging.error(f"Error selecting image: {e}")
        return

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Your Daily Image'
    msg['From'] = args.sender_email
    msg['To'] = args.recipient_email
    msg.set_content('Here is your daily image \u263A \n\n', charset='utf-8')

    # Attach the image
    try:
        with open(full_image_path, 'rb') as img:
            img_data = img.read()
            file_extension = os.path.splitext(img.name)[1]
            mime_type = get_mime_type(file_extension)
            img_name = os.path.basename(img.name)
        msg.add_attachment(img_data, maintype='image', subtype=mime_type, filename=img_name)
    except Exception as e:
        logging.error(f"Error attaching image to email: {e}")
        return

    # Send the email
    try:
        with smtplib.SMTP(args.smtp_server, args.smtp_port) as server:
            server.starttls()
            server.login(args.smtp_user_name, args.smtp_password)
            server.send_message(msg)
            logging.info("Email successfully sent with image.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

# Schedule the task
schedule.every().day.at(args.schedule).do(send_email_with_image)
logging.info("Email server launched and scheduled to send daily emails at 10:00 AM.")

if args.debug.lower() == 'true':
    logging.info("Debug mode is on. Sending a test email immediately.")
    send_email_with_image()

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
