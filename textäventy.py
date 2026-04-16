def room_1():
    print("Du vaknar up i en mörk skog. framför dig finns det två stigar en till vänster och en till höger. Vilken väljer du?")
    choice_1=input("Väljer du högra eller vänstra stigen? ")
    if choice_1=="vänstra":
        room_2()
    elif choice_1=="högera":
        room_3()
    else:
        room_1()

def room_2():
    print("Skogen blir mörkare och mörkare. Du kliver på en pinne. Knak!!! Det känns som att någon kollar på dig sen hör du ett rytande bakom dig. Du springer med allt du har. Framför dig ser du en stuga med lampan på och till din sida ser du ett hål i marken.")
    choice_2=input("Väljer du att springa till stugan eller hålet?")
    if choice_2=="stugan":
        print("Du springer men just innan du hinner fram till stugan så blir du fångad av monstret...")
        gameover_1=input("Vill du spela igen? ja eller nej?")
        if gameover_1=="ja":
            room_1()
        else:
            print("hejdå")
    elif choice_2=="hålet":
        room_4()
    else: 
        room_2()

def room_3():
    print("poopi")
room_1()