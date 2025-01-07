import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and receiver details
sender_email = "elisemcyo@gmail.com"
receiver_email = "benjaminbuntu4@gmail.com"
password = "mmvx qrxa edmf bkez"  # Use the app password here

# Email content
subject = "Your Zodiac Sign"
body = '''
Hello there! The following is your zodiac sign according to your provided date of bith.
You are virgo and we really take for using our website 🙏.
'''

# Create the email
message = MIMEMultipart()
message["From"] = f'ZodiacSignApp {sender_email}'
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)  # Login to your Gmail account
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send email
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")