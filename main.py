# Här skriver du ditt textäventyr
import random
#import verity!


def introduction():
    print("\033c", end="")
    print("booo")





def inventory():
    print("\033c", end="")
    print ("ajjj")



def början():
    global guld
    guld = 25
    print("\033c", end="")
    print ("du heter", (name), "och du är", (age))
    print ("du har", (guld),"kr")
    print ("du har vaknat i ditt hus vad vill du gjöra nu?")
    input ("skriv HELP om du är fast ")


def spelare():
    print("\033c", end="")
    global age
    global name
    name = str(input("what is your namn? "))
    
    age = int(input("what is yo ålder? "))

    

    if age < 16:
        input("gogo gaga du har fel!!!!")
        spelare()

    elif age > 130:
        input("du fick en hjärt attack!")
        

    elif age == str:
        print("välg en riktig ålder")
        spelare()

    else:
        början()

        
spelare()



