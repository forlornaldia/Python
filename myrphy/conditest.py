from doobis import clrcon
from time import sleep

def Level_1():
    print("The man opens the door.")
    sleep(2)
    clrcon()
    print("An old wizard approaches you.")
    sleep(2)
    clrcon()
    begin_quest = input("Are you ready to begin your adventure [y/n] ")
    if begin_quest == "y":
        print("The adventure begins...")
    else: print("You're right, go sleep bozo.")


def Ans():
    password = input("What is the answer to life, the universe and everything? ")
    if password == ("42"):
        print("Welcome wise one. I see you've traveled the galaxy. Let's begin. ")
        Level_1()
    elif(password == "bob"):
        print("This is no time for jokes. ")
    elif(password == "tom"):
        print("Funny cat that runs and chases the dumb idiot mouse. ")
    else:
        print("ur a newbie bozo")

Ans()