from Astrology import ZodiacSign
import pyfiglet

app = pyfiglet.Figlet(font='ansi_regular').renderText('ZODIAC APP')
print(f"\n{pyfiglet.Figlet(font='ansi_regular').renderText('ZODIAC APP')}", end="")

print("~~ Do you know your birthdate? I can tell you which zodiac sign you fall under!😊 ~~\n")

if input("Wanna provide your birth date? (yes/no): ").lower() in ['yes','y']:
    
    user = ZodiacSign(input('Enter your Date of Birth in ISO_FORMAT (YEAR-MONTH-DAY): '))
    print(user.getZodSign())

else: print('Thank you!')