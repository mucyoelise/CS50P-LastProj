from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import re
from datetime import date

class ZodiacSign:
    user_dob = ''
    user_sign = ''
    user_pers = ''
    def __init__(self, dob):
        self.dob = dob
    
    #Make dob property of class
    @property
    def dob(self):
        return self._dob
    
    # Create dob setter
    @dob.setter
    def dob(self, n):
        try:
            if date.fromisoformat(n):
                self._dob = n
                ZodiacSign.user_dob = n
        except Exception as err:
            print('\nError:',err)
            print("Usage: input in this format (Year-Month-Day)")
            print('''
                Year range: "not more than today's year"\t 
                Month range: "01 - 12"\t 
                Day range: "01-lastDayOfMonth"
        ...Note that all the parts (year, month, and day) should be numbers...
                \n''')
            raise()
    
    def __repr__(self):
        return f'\nYour provided DoB is a valid format: "{self._dob}".\nWanna get your ZodiacSign use getZodSign() module.\n'
    
    def getZodSign(self):
        year, month, day = str(self.dob).split('-')

        if date(int(year), 3, 21)<=date(int(year),int(month),int(day))<= date(int(year),4,19):
                ZodiacSign.user_sign = "Aries"
        elif date(int(year), 4, 20)<=date(int(year),int(month),int(day))<= date(int(year),5,10):
                ZodiacSign.user_sign = "Taurus"
        elif date(int(year), 5, 21)<=date(int(year),int(month),int(day))<= date(int(year),6,20):
                ZodiacSign.user_sign = "Gemini"
        elif date(int(year), 6, 21)<=date(int(year),int(month),int(day))<= date(int(year),7,22):
                ZodiacSign.user_sign = "Cancer"
        elif date(int(year), 7, 23)<=date(int(year),int(month),int(day))<= date(int(year),8,22):
                ZodiacSign.user_sign = "Leo"
        elif date(int(year), 8, 23)<=date(int(year),int(month),int(day))<= date(int(year),9,22):
                ZodiacSign.user_sign = "Virgo"
        elif date(int(year), 9, 23)<=date(int(year),int(month),int(day))<= date(int(year),10,22):
                ZodiacSign.user_sign = "Libra"
        elif date(int(year), 10, 23)<=date(int(year),int(month),int(day))<= date(int(year),11,21):
                ZodiacSign.user_sign = "Scorpio"
        elif date(int(year), 11, 22)<=date(int(year),int(month),int(day))<= date(int(year),12,21):
                ZodiacSign.user_sign = "Sagittarius"
        elif date(int(year)-1, 12, 22)<=date(int(year),int(month),int(day))<= date(int(year),1,19):
                ZodiacSign.user_sign = "Capricorn"
        elif date(int(year), 1, 20)<=date(int(year),int(month),int(day))<= date(int(year),2,18):
                ZodiacSign.user_sign = "Aquarius"
        elif date(int(year), 2, 19)<=date(int(year),int(month),int(day))<= date(int(year),3,20):
                ZodiacSign.user_sign = "Pisces"
        print(f'\n\tYour Zodiac Sign is {ZodiacSign.user_sign} 🤓\n')
        return ZodiacSign.getPersonalities()
    
    @classmethod
    def getPersonalities(cls):
        print(f"Do you want to get your personalities too; based on your ZodiacSign ({cls.user_sign})?", end=" ")
        if input().lower() in ['yes','y']:
            with open("personalities.json",mode='r') as aFile:

                pers = json.load(aFile)
            for sign, behavior in pers.items():
                if sign == cls.user_sign:
                    print(f'\nThe following are your personalities based on your zodiac sign "{sign}":\n')
                    for ind, each in enumerate(behavior):
                        cls.user_pers+= f"{ind+1}. {each}\n"
                        print(f"{ind+1}. {each}\n")
                    return cls.receivetoEmail()
                
            else: return "Can't find the file; please try again later!!"

        else: return "It's okay; Thank you!!🥰"

    @classmethod
    def receivetoEmail(cls):
        print("\nDo you want to receive this to your email? We can send it for you! 🥰")
        if input('Your response (yes/no): ').lower() in ['y','yes']:
            # Sender and receiver details
            sender_email = "elisemcyo@gmail.com"
            load_dotenv()
            password = os.getenv("EMAIL_APP_PASSWORD")  # Use the app password here

            while True:     
                if match := re.search(pattern=r"^([a-zA-Z0-9._]+@gmail.com)$", string = input("Please enter your gmail account here: ").strip().lower()):
                    receiver_email = match.group()
                    break
                else:
                    print('Invalid gmail account. Please try again!\n')
            print("Loading.....")
            # Email content
            subject = f"You are {cls.user_sign.upper()}"
            body = f'''
Hello {cls.user_sign}! The following are your personalities according to your Date of Birth ({cls.user_dob}):\n
{cls.user_pers}
We really thank you and appreciate your support for using ZodiacSignApp🙏

            ~~~~~~~~~~~~~~~ All rights reserved by ZodiacSignApp owner. ~~~~~~~~~~~~~~~~~~
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
                    print("\nEmail sent successfully!")
                    return "\n~~~~~~~~~~~~~~~ Thank you for using ZodiacSignApp🙏 ~~~~~~~~~~~~~~~\n"
            except Exception as err:
                return f"Error: {err}"
        else: return "It's okay! Thank you for using ZodiacSignApp🙏"