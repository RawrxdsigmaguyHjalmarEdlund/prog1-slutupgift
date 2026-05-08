def room_1():
    print("Du vaknar up i en mörk skog. framför dig finns det två stigar en till vänster och en till höger. Vilken väljer du?")
    choice=input("Väljer du högra eller vänstra stigen?")
    if choice=="vänstra":
        room_2()
    elif choice=="högra":
        room_3()
    else:
        room_1()

def room_2():
    print("Skogen blir mörkare och mörkare. Du kliver på en pinne. Knak!!! Det känns som att någon kollar på dig sen hör du ett rytande bakom dig. Du springer med allt du har. Framför dig ser du en stuga med lampan på och till din sida ser du ett hål i marken.")
    choice=input("Väljer du att springa till stugan eller hålet?")
    if choice=="stugan":
        print("Du springer men just innan du hinner fram till stugan så blir du fångad av monstret...")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    elif choice=="hålet":
        room_4()
    else: 
        room_2()

def room_3():
    print("Du hör ett rytande vänster om dig, tur att du inte gick ditt. Du ser två till stigar framför dig en till höger och en till vänster.")
    choice=input("Väljer du högra eller vänstra stigen?")
    if choice=="vänstra":
        room_5()
    elif choice =="högra":
        room_6()
    else:
        room_3()
    
def room_4():
    print("Hålet fortsätter framåt. Efter du har krypt ett tag så ser du en öppning till din sida men hålet fortsätter framåt.")
    choice=input("Fortsätter du framåt eller kryper du in i öppningen")
    if choice == "framåt":
        print("Hållet blir tightare och tightare. När du bästemer dig för att krypa till baka så kan du inte du har fastnat i hållet...")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    elif choice_4 == "öppningen": 
        room_7()
    else:
        room_4
def room_5():
    print("stigen fortsätter Du kan framåt men du ser ett ljus åt vänster.")
    choice=input("Vill du gå åt ljuset eller fortsätta på stigen")
    if choice == "ljuset":
        room_8()
    elif choice == "stigen":
        print("Du känner hur du börjar sjunka ner i stigen när du försöker ta dig loss så sjunker du djuppare tills du är helt svald.")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    else:
        room_5
def room_6():
    print("Du ser två igelkott med trollkarls hat?!?!??!")
    print("-Hej vi är trollkarls igelkottarna två Ige och Sige. Vi har en gåtta till dig. Vad får man om man korsar en orm och en igelkott?")
    choice = input("Vad svarar du?")
    if choice == "Taggtråd":
        print("rätt svar duktigt gjort ni får gå ut ifrån dena skogg.")
        print("Du vandrar förbi dom ut ur skogen!!!")
    else:
        print("Du känner hur din kropp förvrids och blir mindre... när du kollar ner på dig själv ser då att du har tasar och spikar på rygen!!!")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
def room_7():
    print("I öpningen ser du en blåbärs buske och en väg up.")
    choice = input("Vill du äta ett blåbär eller vill du fortsätta.")
    if choice == "blåbär":
        print("Du äter ett blåbär sedan fortsätter du.")
        room_9()
    elif choice == "fortsätta": 
        room_9()
    else:
        room_7
def room_8():
    print("ljuset värkar ha kommit från en stuga åt höge och en stig finns åt vänster")
    choice =input("Vill du gå in i stugan eller gå in i stigen?")
    if choice == "stigen":
        room_10()
    elif choice == "stugan":
        room_12()
    else:
        room_8()
def room_9():
    print("Du fortsätter up upp från öppningen när du stiker up huvudet. Ser du tre saker. En dör, En katt och en Gorilla med ett kort deck.")
    choice = input("Vill du gå till dören, katten eller gorillan? ")
    if choice == "dören":
        room_13()
    elif choice == "katten":
        room_14
    elif choice == "gorillan":
        room_15
    else:
        room_9()
def room_10():
    print("Du kan fortsätta på stigen eller krypa in i ett hål höger om dig.")
    choice = input("Vill du fortsätta på stigen eller gå in i hålet? ")
    if choice == "stigen":
        room_11()
    if choice == "hålet":
        room_4()
    else:
        room_10()
def room_11():
    print("Du går några steg sedan stopar stigen du vänder dig om och ser två stigar.")
    choice=input("Väljer du högra eller vänstra stigen?")
    if choice=="vänstra":
        room_2()
    elif choice=="högra":
        room_3()
    else:
        room_11()
def room_12():
    print("När du öppnar dörren ser du en häxa.")
    print("-Hej jag är häxa stor näsa. Du ska svara på mina gåter 10 annars så äter jag up dig.")
    guess=input("Vad blir blötare ju mer den torkar? ")
    if guess=="handduk":
        print("duktig men jag har en till gåta för dig")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    guess=input("Vad har fyra ben men kan inte gå? ")
    if guess=="bord":
        print("rätt men du har fortfarande 8 kvar.")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    guess=input("Vad kan resa runt hela världen utan att lämna sitt hörn? ")
    if guess=="frimärke":
        print("7 kvar.")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    guess=input("Vad går upp men aldrig ner? ")
    if guess=="ålder":
        print("du är bra, bara 6 kvar.")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    guess=input("Vad har ett öga men kan inte se? ")
    if guess=="nål":
        print("hälften klar bra jobbat.")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    guess=input("Vad blir större ju mer man tar bort från det? ")
    if guess=="hål":
        print("Jag hoppas du får fel snart min mage kurar, 4 kvar.")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    guess=input("Vad kan man fånga men inte kasta? ")
    if guess=="förkylning":
        print("3 kvar...")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    guess=input("Vad har många tänder men kan inte bita? ")
    if guess=="kam":
        print("2 kvar...")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    guess=input("Vad är fullt av hål men håller ändå vatten? ")
    if guess=="svamp":
        print("1 kvar...")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    guess=input("Vad är det som alltid kommer mot dig men aldrig fram? ")
    if guess=="morgondagen":
        print("Hur är det möjligt ingen har klarat det tidigare åh nej.")
        print("Hexan blir till aska precis som spider man i infinty war eller end game kom inte ihåg vilken. där hon stod ligger det nu en nyckel. Du tar upp den och låser upp back dören när du öppnar den är du tillbaka till ditt rum.")
        input("Du vann vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")
    else:
        print("Fel nu ätter jag upp dig mohahha")
        gameover=input("Vill du spela igen? ja eller nej?")
        if gameover=="ja":
            room_1()
        else:
            print("hejdå")

    
    
def room_13():
    print("Du går till dören och öppnar den ser du ett mörker på andra sidan.")
    input("går du i? [ja/nej]")
room_1()
