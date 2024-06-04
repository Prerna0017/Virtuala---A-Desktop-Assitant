# Happy Birthday in Python Code 
from datetime import date
import time
from random import randint
import pyttsx3
from playsound import playsound
import threading



def bdyWish():
    bday_year = 2003
    todays_date = date.today()
    age = todays_date.year - bday_year

    for i in range(1,85):
        print('')

    space = ''


    for i in range(1,75):
        count = randint(1, 100)
        while(count > 0):
            space += ' '
            count -= 1

        if(i%10==0):
            print(space + '🎂Happy Birthday!')
        elif(i%9 == 0):
            print(space + "🎂")
        elif(i%5==0):
            print(space +"💛")
        elif(i%8==0):
            print(space + "🎉")
        elif(i%7==0):
            print(space + "🍫")
        elif(i%6==0):
            print(space + "Happy",age,"th Birthday!💖")
        else:
            print(space + "🔸")

        space = ''
        time.sleep(0.2)

def bdySong():
    time.sleep(0.001)
    try:
        playsound('C:/Users/Jadhav/Desktop/Final Year Project/ChatBot/happybday.mp3')
    except:
        print("Ignore") 

def checkBdy():
    bday_day = 90
    bday_month = 3
    bday_year = 2003

    todays_date = date.today()

    if (int(todays_date.day) == bday_day):
        if (int(todays_date.month) == bday_month):

            # age = todays_date.year - bday_year

            display = threading.Thread(target = bdyWish, args=())
            wish = threading.Thread(target = bdySong, args=())
            display.start()
            wish.start()
    else:
        # print("Sorry , its not your birthday today")
        print("")

# checkBdy()