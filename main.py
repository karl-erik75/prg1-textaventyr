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
    elif val == "spela med pengar" or val == "spela":
        input("du välger att spela black jack")
        gm = int(input(" du har", (guld), "hur mycket pengar läger du in? "))
        if gm > guld:
            print("du har inte så ,ycket pengar!")
            saloon()
        elif gm < guld or gm == guld:
            gmstart = random.randint (1,13)
            gmstart2 = random.randint (1,13)
            if gmstart == 1:
                gmstart = 10

            elif gmstart == 2:
                gmstart = 10

            elif gmstart == 3:
                gmstart = 10

            elif gmstart == 4:
                gmstart = 10

            elif gmstart == 5:
                gmstart = 11

            elif gmstart == 6:
                gmstart = 2

            elif gmstart == 7:
                gmstart = 3

            elif gmstart == 8:
                gmstart = 4

            elif gmstart == 9:
                gmstart = 5

            elif gmstart == 10:
                gmstart = 6

            elif gmstart == 11:
                gmstart = 7

            elif gmstart == 12:
                gmstart = 8

            elif gmstart == 13:
                gmstart = 9


            if gmstart2 == 1:
                gmstart2 = 10

            elif gmstart2 == 2:
                gmstart2 = 10

            elif gmstart2 == 3:
                gmstart2 = 10

            elif gmstart2 == 4:
                gmstart2 = 10

            elif gmstart2 == 5:
                gmstart2 = 11

            elif gmstart2 == 6:
                gmstart2 = 2

            elif gmstart2 == 7:
                gmstart2 = 3

            elif gmstart2 == 8:
                gmstart2 = 4

            elif gmstart2 == 9:
                gmstart2 = 5

            elif gmstart2 == 10:
                gmstart2 = 6

            elif gmstart2 == 11:
                gmstart2 = 7

            elif gmstart2 == 12:
                gmstart2 = 8

            elif gmstart2 == 13:
                gmstart2 = 9

            starting_points = gmstart2 + gmstart
            if starting_points > 21:
                starting_points = 21
            print ("du har", (starting_points))
            gmstart = random.randint (1,13)
            gmstart2 = random.randint (1,13)
            if gmstart == 1:
                gmstart = 10

            elif gmstart == 2:
                gmstart = 10

            elif gmstart == 3:
                gmstart = 10

            elif gmstart == 4:
                gmstart = 10

            elif gmstart == 5:
                gmstart = 11

            elif gmstart == 6:
                gmstart = 2

            elif gmstart == 7:
                gmstart = 3

            elif gmstart == 8:
                gmstart = 4

            elif gmstart == 9:
                gmstart = 5

            elif gmstart == 10:
                gmstart = 6

            elif gmstart == 11:
                gmstart = 7

            elif gmstart == 12:
                gmstart = 8

            elif gmstart == 13:
                gmstart = 9


            if gmstart2 == 1:
                gmstart2 = 10

            elif gmstart2 == 2:
                gmstart2 = 10

            elif gmstart2 == 3:
                gmstart2 = 10

            elif gmstart2 == 4:
                gmstart2 = 10

            elif gmstart2 == 5:
                gmstart2 = 11

            elif gmstart2 == 6:
                gmstart2 = 2

            elif gmstart2 == 7:
                gmstart2 = 3

            elif gmstart2 == 8:
                gmstart2 = 4

            elif gmstart2 == 9:
                gmstart2 = 5

            elif gmstart2 == 10:
                gmstart2 = 6

            elif gmstart2 == 11:
                gmstart2 = 7

            elif gmstart2 == 12:
                gmstart2 = 8

            elif gmstart2 == 13:
                gmstart2 = 9
            Fstarting_points = gmstart2 + gmstart
            if Fstarting_points > 21:
                Fstarting_points = 21
            print ("din fiende har", (Fstarting_points))
            
                

            

        

        poängdam = 10 # 10 points (de fins 4)
        poängkung = 10 # 10 points (de fins 4)
        poängknektar = 10 # 10 points (de fins 4)
        poångA = 11 # 11 points (de fins 4)
        poäng2 = 2 #2 points (de fins 4)
        poäng3 = 3 #3 points (de fins 4)
        poäng4 = 4 #4 points (de fins 4)
        poäng5 = 5 #5 points (de fins 4)
        poäng6 = 6 #6 points (de fins 4)
        poäng7 = 7 #7 points (de fins 4)
        poäng8 = 8 #8 points (de fins 4)
        poäng9 = 9 #9 points (de fins 4)
        poäng10 = 10 #10 points (de fins 4)



        
            


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
