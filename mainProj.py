from datetime import date
def main():
    while True:
        userdob= input("Enter your date of birth: ")
        try:
            if date.fromisoformat(userdob):
                year, month, day = userdob.split('-')
                    
                if date(int(year), 3, 21)<=date(int(year),int(month),int(day))<= date(int(year),4,19):
                        user_sign = "Aries"
                elif date(int(year), 4, 20)<=date(int(year),int(month),int(day))<= date(int(year),5,10):
                        user_sign = "Taurus"
                elif date(int(year), 5, 21)<=date(int(year),int(month),int(day))<= date(int(year),6,20):
                        user_sign = "Gemini"
                elif date(int(year), 6, 21)<=date(int(year),int(month),int(day))<= date(int(year),7,22):
                        user_sign = "Cancer"
                elif date(int(year), 7, 23)<=date(int(year),int(month),int(day))<= date(int(year),8,22):
                        user_sign = "Leo"
                elif date(int(year), 8, 23)<=date(int(year),int(month),int(day))<= date(int(year),9,22):
                        user_sign = "Virgo"
                elif date(int(year), 9, 23)<=date(int(year),int(month),int(day))<= date(int(year),10,22):
                        user_sign = "Libra"
                elif date(int(year), 10, 23)<=date(int(year),int(month),int(day))<= date(int(year),11,21):
                        user_sign = "Scorpio"
                elif date(int(year), 11, 22)<=date(int(year),int(month),int(day))<= date(int(year),12,21):
                        user_sign = "Sagittarius"
                elif date(int(year), 12, 22)<=date(int(year),int(month),int(day))<= date(int(year),1,19):
                        user_sign = "Capricorn"
                elif date(int(year), 1, 20)<=date(int(year),int(month),int(day))<= date(int(year),2,18):
                        user_sign = "Aquarius"
                elif date(int(year), 2, 19)<=date(int(year),int(month),int(day))<= date(int(year),3,20):
                        user_sign = "Pisces"
                break
            else:
                print("Wrong format!")

        except Exception as e:
            print('\nError:',e)
            print("Usage: input in this format (Year-Month-Day)")
            print('''
                Year range: "not more than today's year"\t 
                Month range: "01 - 12"\t 
                Day range: "01-lastDayOfMonth"\n''')
    print("Your ZodiacSign based on entered date of birth is:", user_sign)
    print("Wanna know your personalities based on your ZodiacSign (y/n): ", end="")
    if not input().lower in ["yes", "y","no","n"]:
        exit()

if __name__ == '__main__':
    main()