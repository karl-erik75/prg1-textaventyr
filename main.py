# Här skriver du ditt textäventyr
import random
#import verity!
global knife
knife = True
global rev
rev = False
global honor 
honor = 0

global mjölk
global H_wisky
global vin
global wisky
mjölk = 0
H_wisky = 0
vin = 0
wisky = 0
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
#-----------------------------------------------------
def DEATH():
    print("\033c", end="")
    input("du är död du måste börja om")
    print("\033c", end="")
#-----------------------------------------------------
#-----------------------------------------------------
def vinst():
    input("skotet gick rakt igenom hans huvud DU VAN!!!!!")
    global Qrysk
    Qrysk = True
    fråga()
#----------------------------------------------------
global Qrysk
#dom olika stälerna man kan gå till
#-----------------------------------------------------
def saloon():
    print("\033c", end="")
    stats()
    val = input("vad vill du gjöra (sköpa en drika) (prata med folk) (spela med pengar). skriv (annat) om du vil bort! ")

    #första valet om du välgjer drika
    #----------------------------------------------------- 
    if val == "sköp en drika" or val == "drika":
        
        drika = input("vilken drika vil du sköpa? (hård wisky), (wisky), (vin). (mjölk) ")
        if drika == "hård wisky":
            print("vill du drika den nu?")
            global H_wisky
            H_wisky = H_wisky + 1

        elif drika == "wisky":
            print("vill du drika den nu?")
            global wisky
            wisky = wisky + 1

        elif drika == "vin":
            print ("vill du drika den nu?")
            global vin
            vin = vin + 1
        elif drika == "mjölk":
            print ("vill du drika den nu?")
            global mjölk
            mjölk = mjölk + 1
        else:
            input("du skrev något fel")
            saloon()
    #-----------------------------------------------------

    #om du spelar med moneyyyy
    #-----------------------------------------------------
    elif val == "spela med pengar" or val == "spela":
        print("\033c", end="")
        input("rusian rulet")
        mon = random.randint (2,5)
        vinsten = 500    
        vinst_pengar = vinsten * mon
        print("priset är", vinst_pengar)
        val23 = input("är du säker att du vil spela? ")
        if val23 == "nej":
            input("du valde att gå till baka")
            saloon()
        elif val23 == "ja":
            skot = 0
            spelet = False
            print("\033c", end="")
            input("В пистолете один патрон; в каждом раунде вы либо стреляете в себя, либо прокручиваете барабан и затем стреляете в себя.")
            input("han sa något oviktigt om reglerna")
            input("han läger ett skot i pistolen och snurar på cylinder sedan ger han dig pistolen")
            cylinder = random.randint(1,6)
            spelet = True
            while spelet == True:
                print("\033c", end="")
                val3 = input("vad gjör du (skjuta eller snura) ")
                if val3 == "skjuta":
                    skot = skot + 1
                    if cylinder == skot:
                        print("\033c", end="")
                        input("wasted! du dog av at skjuta dig skälv :(")
                        spelet = False
                        DEATH()
                    elif cylinder != skot:
                        input("du hörde ett click sedan gede du revolvern åt han")
                        if skot == 5:
                            print("han valde att snura cylinder")
                            cylinder = random.randint(1,6)
                            skot = 0
                            skot = skot + 1
                            if skot == cylinder:
                                spelet = False
                                vinst()
                            else:
                                input("ni hörde ett click och fortsete sköra")
                        else:
                            input("han valde att skjuta sig skälv")
                            skot = skot + 1
                            if skot == cylinder:
                                spelet = False
                                vinst()
                            else:
                                input("ni hörde ett click och forsäte att spela")
                        
                        
                elif val3 == "snura":
                    input("du valde att snura cylindern")
                    cylinder = random.randint(1,6)
                    skot = 0
                    input("du rikta pistolen mt digskälv")
                    skot = skot + 1
                    if skot == cylinder:
                        DEATH()
                    elif skot != cylinder:
                        input("du hörde ett click sedan gede du revolvern åt han")
                        if skot == 5:
                            print("han valde att snura cylinder")
                            cylinder = random.randint(1,6)
                            skot = 0
                            skot = skot + 1
                            if skot == cylinder:
                                spelet = False
                                vinst()
                            else:
                                input("ni hörde ett click och fortsete sköra")

                        else:
                            input("han valde att skjuta sig skälv")
                            skot = skot + 1
                            if skot == cylinder:
                                spelet = False
                                vinst()
                            else:
                                input("ni hörde ett click och forsäte att spela")


        else:
            print("du skrev något fel")
            saloon()      


    #quests/om du vil prata med folk
    #-----------------------------------------------------
    elif val == "prata" or val == "prata med folk":

        personer = random.randint(1,6)
       


        #-----------------------------------------------------
        if personer == 5:
            input("Psst! Jam 17 vjeç dhe nuk mund të blej armë zjarri... a mund të ma blesh ti një? Mund të të paguaj shumë mirë. ") #sköp ett stort vapen till han
            if Qvapen == False:
                input("han vil ha en stor pistol")
            elif Qvapen == True:
                input("du klarade det!")
            saloon()

        
        elif personer == 4:
            input("Whisky nukillaangasoq isumaqarpunga. Nassaarisinnaagukku nukittunerusumik tunisinnaaviuk? ") #hita hårdare wisky
            if Qwisky == False:
                input("han vill at du ska skåpa hårdare wisky en vad dom har här")

            elif Qvapen == True:
                print("ajj")
            saloon()

        elif personer == 3:
            input("Иктаж-могай руш дене тӱкнен улыда? Нуно Олимпиадым бомбитлаш шонат. КАЖНЕ РУШЫМ ПУШТЫЗА!") # döda en rysk!
            if Qrysk == False:
                input("han vill att du ska döda en rysk")
            elif Qrysk == True:
                input("han nickade och sa att han var stålt")
                global guld
                guld = guld + 200
                global honor
                honor = honor - 1

            saloon()

        elif personer == 2:
            input("茶色い狼を見なかったか？俺の足の親指を食いちぎりやがったんだ！そいつの首を持ってきてくれれば、200払ってやるぞ！") #brun varg ska dödas!
            if Qbrunvarg == False:
                input("han vill at du sak döda en brun varg")
            elif Qbrunvarg == True:
                print("ok!!!")
            saloon()

        elif personer == 1:
            input("Hei, jeg er kanskje litt for ung til å kjøpe whisky. Du ser ut som en snill, eldre mann – kunne du kjøpt en til meg? Jeg har pengene...") #SKöp wiskin
            if Qwisky2 == False:
                input("sköp en normal wisky åt han")
            if Qwisky2 == True:
                print("ajkjjjdzopjneijpf")

        elif personer == 6:
            input("jamen tjena brosan! mit namn är Ulf. Ulf Ulfsson amen kalla mig bara ulf då. Du du ser ut som en god medborgare skule du kuna ge mig lite fika?") # FIAKKAKAKAKAKKAKAA
            if Qfika == False:
                input("hitta han fika! (((TIPS!!! hjälp han SIST!!!)))")
            elif Qfika == True:
                print("rysk")
            saloon()
            #-----------------------------------------------------
    #-----------------------------------------------------

    #-----------------------------------------------------
    elif val == "annat":
        fråga()
    #-----------------------------------------------------
    #-----------------------------------------------------
    else:
        input("du skrev något fel")
        saloon()
    #-----------------------------------------------------
#-----------------------------------------------------
def casino():
    print("\033c", end="")
    if Qbrunvarg == False:
        stats()
        input("woof woof woof WOOF (säger den bruna vargen som äger casinot)")
        val = input("vid vil du spela? (slots) eller (slots) eller (annat) om du vil härifrån? ""alla andra maskiner är trasiga""")
        if val == "slots":
            print("du valde ATT SPELA SLOTS")
            slots = True
            while slots == True:
                print("\033c", end="")
                money = int(input("how mutch money vill du läga in?"))
                if money == guld or money < guld:
                   
                    global guld
                    guld = guld - money
                    tal1 = random.randint(1,3)
                    tal2 = random.randint(1,3)
                    tal3 = random.randint(1,3)
                    if tal1 == 1:
                        tal1 = "strawbery"
                    elif tal1 == 2:
                        tal1 = "cherry"
                    elif tal1 == 3:
                        tal1 = "seven"

                    if tal2 == 1:
                        tal2 = "strawbery"
                    elif tal2 == 2:
                        tal2 = "cherry"
                    elif tal2 == 3:
                        tal2 = "seven"

                    if tal3 == 1:
                        tal3 = "strawbery"
                    elif tal3 == 2:
                        tal3 = "cherry"
                    elif tal3 == 3:
                        tal3 = "seven"

                    print ((tal1), (tal2), (tal3))
                    if tal1 == tal2 and tal2 == tal3 and tal1 == "strawbery":
                        money = money * 7
                        print("you won", (money))
                        global guld
                        guld = guld + money



                    print ((tal1), (tal2), (tal3))
                    if tal1 == tal2 and tal2 == tal3 and tal1 == "cherry":
                        money = money * 7
                        print("you won", (money))
                        global guld
                        guld = guld + money

                    print ((tal1), (tal2), (tal3))
                    if tal1 == tal2 and tal2 == tal3 and tal1 == "seven":
                        money = money * 7
                        print("you won", (money))
                        global guld
                        guld = guld + money

                    else:
                        input("du förlorade :(")
                        

                    
                        

                    

                        



                else:
                    input("du är för fatig brokie!")
                    slots = False
                    casino()




        elif val == "annat":
            fråga()

        else:
            input("du skrev något fel")
            casino()
            
            
    


Qrysk = False

global Qwisky
Qwisky = False

global Qbrunvarg
Qbrunvarg = False

global Qwisky2
Qwisky2 = False

global Qfika
Qfika = False

global Qvapen
Qvapen = False


#started av spelet
#-----------------------------------------------------
introduction()
#-----------------------------------------------------
