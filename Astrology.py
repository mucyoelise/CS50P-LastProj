from datetime import date
class ZodiacSign:
    def __init__(self, dob):
        self.__dob = dob

    def zodiac(self):
        

        pass

while True:
    userdate= input("Enter your date of birth: ")
    try:
        if date.fromisoformat(userdate):
            print(userdate)
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

print('Done!')
