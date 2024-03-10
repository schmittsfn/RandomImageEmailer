# Random Image Emailer

## Overview

The Random Image Emailer is a Python script designed to automate the process of sending emails with a randomly selected image attachment. It's perfect for newsletters, daily greetings, marketing campaigns, or simply sharing interesting images from a curated collection with friends, family, or clients. The script is equipped with scheduling capabilities, allowing you to specify the exact time for sending out emails daily. Additionally, it supports command-line arguments for flexible configuration of email settings and the image directory path.

## Features

- **Random Image Selection:** Automatically picks a random image from a specified directory to send via email.
- **Daily Scheduling:** Sends out an email with a randomly selected image attachment at a specified time each day.
- **Immediate Test Email:** Sends an initial test email upon launch to verify that the configuration works as expected.
- **Command-Line Configuration:** Easily configure sender and recipient email addresses, SMTP server details, and the image directory path through command-line arguments.
- **Logging:** Provides detailed logging for each step of the process, including successful email transmission and potential errors.

## Installation

To use the Random Image Emailer, you need Python 3 installed on your system. Additionally, you'll need to install the `schedule` and `imagesize` packages. You can install these dependencies by running:

```bash
pip install schedule imagesize
```

## Usage

1. **Prepare Your Images:** Place all the images you want to potentially send out in a single directory. The script will randomly select from these images for each email sent.

2. **Configure and Run:** Use the command-line to configure and launch the script. Here's an example command:

```bash
python random_image_emailer.py --sender-email your_email@example.com --recipient-email recipient_email@example.com --smtp-server smtp.example.com --smtp-port 587 --smtp-user-name smtp_user_name --smtp-password your_password --image-dir /path/to/your/images --schedule the_time --debug true
```

Replace the placeholders with your actual information:

- `--sender-email`: Your email address.
- `--recipient-email`: The email address of the recipient.
- `--smtp-server` and `--smtp-port`: Your SMTP server address and port.
- `--smtp-user-name`: The user name for your SMTP server.
- `--smtp-password`: The password for your SMTP server.
- `--image-dir`: The path to the directory containing your images.
- `--schedule`: The time when the email should be sent daily.
- `--debug`: Whether to toggle debugging mode which sends out an email immediately.

3. **Verify Initial Email:** Upon launch, the script will send an initial test email. Verify that this email is received to ensure everything is set up correctly.

4. **Scheduled Emails:** After the initial test email, the script will continue running and send an email with a randomly selected image every day at the specified time.

## Security Note

For security reasons, avoid hardcoding sensitive information like email passwords directly into the script. Consider using environment variables or a secure method to pass these values.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to fork the repo, make changes, and submit a pull request.

---

This README provides a comprehensive guide to help users understand, install, and use the Random Image Emailer. Modify it as needed to better fit your project's specifics or personal preferences.


## SMTP setup using AWS

Configuring Amazon SES to use its SMTP service involves several steps:

**Setting Up Your SES Account:**

* Sign up for an AWS account or log in to your existing account.
* Verify your domain identity in SES to ensure you have permission to send emails from that domain.
* If necessary, request production access for increased sending limits.

**Creating SMTP Credentials:**

* In the SES console, navigate to the "SMTP Settings" section.
* Click "Create My SMTP Credentials". This generates a unique username and password for your AWS region. You'll need these credentials to connect your server to SES.

**Configuring Your Server:**

* Locate your server's email sending library or script.
* Update the configuration to use the following details:
    * SMTP Endpoint: The specific endpoint URL for your AWS region (e.g., [invalid URL removed]).
    * Port: You can choose either port 25 or 587 depending on your server's security configuration and your needs. Port 587 typically requires STARTTLS encryption.
    * Authentication: Set the authentication method to "Plain".
    * Username and Password: Use the SMTP username and password you generated in step 2.

**Sending a Test Email:**

* Once the configuration is complete, you can send a test email from your server using the configured SMTP settings.
* Verify that the email arrives at its destination successfully.

**Additional Resources:**

* Using the Amazon SES SMTP interface: [https://repost.aws/knowledge-center/ses-set-up-connect-smtp](https://repost.aws/knowledge-center/ses-set-up-connect-smtp)
* Amazon SES documentation: [https://docs.aws.amazon.com/ses/](https://docs.aws.amazon.com/ses/)
* How to send an email – Amazon Web Services (AWS): [https://aws.amazon.com/ses/](https://aws.amazon.com/ses/)

**Important Notes:**

* Remember to keep your SMTP credentials secure.
* Consider using a secure connection (STARTTLS) when sending emails through port 587.
* AWS SES offers various features and settings for managing your email sending. Explore the documentation for more advanced configuration options.
