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
    
    @property
    def dob(self):
        return self._dob
    
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
        elif date(int(year), 12, 22)<=date(int(year),int(month),int(day))<= date(int(year),1,19):
                ZodiacSign.user_sign = "Capricorn"
