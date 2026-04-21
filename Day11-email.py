import smtplib
from email.mime.text import MIMEText

# your details
sender_email = "doulatvalmani@gmail.com"
app_password = "################"  # paste your app password
receiver_email = "doulatvalmani@gmail.com"    # send to yourself first!

# create the email
subject = "My First Python Email!"
body = "Hello! This email was sent using Python. I am learning AWS SES!"

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

# send it!
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully! Check your Gmail inbox!")
except Exception as e:
    print(f"Error: {e}")
