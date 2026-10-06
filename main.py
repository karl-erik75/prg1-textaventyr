# Här skriver du ditt textäventyr
import random
#import verity!
global knife
knife = True
global rev
rev = False
global honor 
honor = 0
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

    #första valet om du välgjer drika
    #----------------------------------------------------- 
    if val == "sköp en drika" or val == "drika":
        
        drika = input("vilken drika vil du sköpa? (hård wisky), (wisky), (vin). (mjölk) ")
        if drika == "hård wisky":
            print("du har en hård wisky")

        elif drika == "wisky":
            print("du dör mindre")

        elif drika == "vin":
            print ("de blev en björ och du DÖR")
        elif drika == "mjölk":
            print ("MUMS!!!")
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
                    skot + 1
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
                            skot + 1
                            if skot == cylinder:
                                spelet = False
                                vinst()
                            else:
                                input("ni hörde ett click och fortsete sköra")
                        else:
                            input("han valde att skjuta sig skälv")
                            skot + 1
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
                    skot + 1
                    if skot == cylinder:
                        DEATH()
                    elif skot != cylinder:
                        input("du hörde ett click sedan gede du revolvern åt han")
                        if skot == 5:
                            print("han valde att snura cylinder")
                            cylinder = random.randint(1,6)
                            skot = 0
                            skot + 1
                            if skot == cylinder:
                                spelet = False
                                vinst()
                            else:
                                input("ni hörde ett click och fortsete sköra")

                        else:
                            input("han valde att skjuta sig skälv")
                            skot + 1
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
                print("ok")

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
                input("hitta han fika!")
            elif Qfika == True:
                print("rysk")
            saloon()
            

            #-----------------------------------------------------
#-----------------------------------------------------

#-----------------------------------------------------
def DEATH():
    print("\033c", end="")
    input("du är död du måste börja om")
    print("\033c", end="")
#-----------------------------------------------------
#-----------------------------------------------------
def vinst():
    print("whoa danger u won!")
#----------------------------------------------------
global Qrysk
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
