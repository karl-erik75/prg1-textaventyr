# Här skriver du ditt textäventyr
import random
#import verity!
global knife
knife = True
global rev
rev = False
# (en gångs saker)
print("\033c", end="")
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
        spelare()
        

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



    za_worldo = input("vart vill du gå? (casino), (saloon), (general store), (jobb), något annat ")
    if za_worldo == "saloon":
        saloon()

    elif za_worldo == "casino":
        print(wip)

    elif za_worldo == "general store":
        print(wip)

    elif za_worldo == "jobb":
        print(wip)
    else:
        input("du skrev något fell")
        värld()
#-----------------------------------------------------
#-----------------------------------------------------
def inventory():
    print("\033c", end="")
    print ("du har", (guld),"pengar")
    if rev == True:
        print("du har en revolver med", (bul),"skot")
    
    fråga()
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
    print("<(*)>---------------------------<(*)>")
    print("    namn: ",(name),    "ålder: ",(age))
    print("    du har", (guld), "pengar")
    hp = 30
    if hp > 30:
        hp = 30
        
    print("    du har", (hp), "liv")
    
    
    if rev == True:
        print("    du har en revolver med", (bul))
    else:
        print("    din fika är tom")
    
    if knife == True:
        print("    du har en kniv")
    else:
        print("    din fika är tom")
    print("<(*)>---------------------------<(*)>")
#-----------------------------------------------------

#dom olika stälerna man kan gå till
#-----------------------------------------------------
def saloon():
    print("\033c", end="")
    stats()
    val = input("vad vill du gjöra (sköpa en drika) (prata med folk) (spela med pengar). skriv (annat) om du vil bort! ")

    #första faleet om du välgjer drika
    #----------------------------------------------------- 
    if val == "sköp en drika" or val == "drika":
        
        drika = input("vilken drika vil du sköpa? (hård wisky), (wisky), (vin). (mjölk) ")
        if drika == "HÅRD WISKY!!!":
            print("DU DÖRRRRRR")

        elif drika == "wisky":
            print("du dör mindre")

        elif drika == "vin":
            print ("de blev en björ och du DÖR")
        elif drika == "mjölk":
            print ("MUMS!!!")
        else:
            input("du skrev något fel")
            saloon()
    #quests/om du vil prata med folk
    #-----------------------------------------------------
    elif val == "prata" or val == "prata med folk":
        personer = random.randint(1,6)

        if personer == 5:
            print("Psst! Jam 17 vjeç dhe nuk mund të blej armë zjarri... a mund të ma blesh ti një? Mund të të paguaj shumë mirë. ") #sköp ett stort vapen åt han
        elif personer == 4:
            print("Whisky nukillaangasoq isumaqarpunga. Nassaarisinnaagukku nukittunerusumik tunisinnaaviuk? ") #hita hördare wisky
        elif personer == 3:
            print("Иктаж-могай руш дене тӱкнен улыда? Нуно Олимпиадым бомбитлаш шонат. КАЖНЕ РУШЫМ ПУШТЫЗА!") # döda en rysk!
        elif personer == 2:
            print("茶色い狼を見なかったか？俺の足の親指を食いちぎりやがったんだ！そいつの首を持ってきてくれれば、200払ってやるぞ！") #brun varg ska dödas!
        elif personer == 1:
            print("Hei, jeg er kanskje litt for ung til å kjøpe whisky. Du ser ut som en snill, eldre mann – kunne du kjøpt en til meg? Jeg har pengene...") #SKöp wiskin
        elif personer == 6:
            print("jamen tjena brosan! mit namn är Ulf. Ulf Ulfsson amen kalla mig bara ulf då. Du du ser ut som en god medborgare skule du kuna ge mig lite fika?")






#-----------------------------------------------------







#started av spelet
#-----------------------------------------------------
introduction()
#-----------------------------------------------------
