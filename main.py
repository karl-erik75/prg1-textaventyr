# Här skriver du ditt textäventyr
import random
#import verity!
global knife
knife = True
# (en gångs saker)
#-----------------------------------------------------
def titta_start():
    print("\033c", end="")
    global rev
    rev = True
    global bul
    bul = 3
    print("du tittar runt ditt hus och du tar up din pistol/revolver")
    print("du har", (bul), "skott")
    fråga()
#-----------------------------------------------------
#-----------------------------------------------------
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
#-----------------------------------------------------
#-----------------------------------------------------
def introduction():
    print("\033c", end="")
    input("du är en cowboy i dena värld under 1500 talet i Nordamerica. Du välger skälv vad du heter och   din ålder. du kan skälv välga vad du vill gjöra i dena värld")
    spelare()
#-----------------------------------------------------
#-----------------------------------------------------
def början():
    global guld
    guld = 25
    print("\033c", end="")
    print ("du heter", (name), "och du är", (age))
    print ("Du har", (guld),"pengar.")
    print ("Du har vaknat i ditt hus vad vill du gjöra nu?")
    information = input ("Skriv hjälp om du är fast. ")
    if information == "hjälp":
        information2 = input("Skriv (värld) för att gå till et annat stäle. "
        "(rygsäck) för att se vad du har.(titta) om du vill tita runt ditt hus ")
        if information2 ==  "värld":
            värld()
        
        elif information2 ==  "rygsäck":
            inventory()
        
        elif information2 ==  "titta":
            titta_start()

        else:
            input("du skrev något fell")
            början()
    elif information ==  "värld":
        värld()

    elif information ==  "rygsäck":
        inventory()

    elif information ==  "titta":
        titta_start()
    else:
        input("du skrev något fell")
        början()
#-----------------------------------------------------



# (kommer att envändes igen)
#-----------------------------------------------------
def värld():
    print("\033c", end="")



    print("slut")
#-----------------------------------------------------
#-----------------------------------------------------
def inventory():
    print("\033c", end="")
    print ("du har", (guld),"pengar")
    if rev == True:
        print("du har en revolver med", (bul),"skot")
    else:
        fråga
#-----------------------------------------------------
#-----------------------------------------------------
def fråga():
    print ("vad vill du gjöra nu?")
    information = input("Skriv hjälp om du är fast. ")
    if information == "hjälp":
        information2 = input("Skriv (värld) för att gå till et annat stäle. "
        "(rygsäck) för att se vad du har. ")
        if information2 ==  "värld":
            värld()
        
        elif information2 ==  "rygsäck":
            inventory()
        else:
            input("du skrev något fel")
            fråga()

    
        

        
    elif information ==  "värld":
        värld()

    elif information ==  "rygsäck":
        inventory()
    else:
        print("du skrev något fel")
        fråga()
#-----------------------------------------------------
#-----------------------------------------------------
def stats():
    print("<(*)>-------------------------------------<(*)>")
    print("namn = ", (name), "ålder = ", (age))
    print("du har", (guld), "pengar")
    if rev == True:
        print ("du har en revolver med", (bul))
    if knife == True:
        print ("du har en kniv")
#-----------------------------------------------------










#started av spelet
#-----------------------------------------------------
introduction()
#-----------------------------------------------------
