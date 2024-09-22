# Email Alert System

This project allows you to send email alerts using Python. It includes the `alert.py` script to send emails using the `mailer.py` utility.

## How to Run

1. Start the SMTP debugging server:
   ```bash
   python -m smtpd -n -c DebuggingServer localhost:1025
