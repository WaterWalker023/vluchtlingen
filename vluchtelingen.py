import random 
import time
print()

def vraag1():

    print("\nIs er onrust in jou land? \n \nA: ja: grote onrust \nB: nee \n")
    antwoord1 = input("kies A of B==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("")
        vraag2()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("Wat fijn voor je, je bent veilig")

    else:
        print("\nkies A of B")
        vraag1()

def vraag2():
    print("\nzou je willen vluchten \n \nA: ja graag zo snel mogelijk\nB: nee \n")
    antwoord1 = input("kies A of B ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je gaat nu naar buiten")
        vraag3()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("breng jezelf in veiligheid")

    else:
        print("\nkies A of B")
        vraag2()

def vraag3():  
    print("ben je alleen of ben je met meerdere personen \n \nA: ik ben alleen \nB: samen met mijn moeder \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je pakt hoogstnoodzakelijke spullen")
        vraag4()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je sleurt je ouders mee")
        vraag12()

    else:
        print("\nkies A of B")
        vraag3()

def vraag4():  
    print("ben je mobiel \n \nA: ja ik heb een auto\nB: nee \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je stopt de spullen in je auto en rijdt weg")
        vraag5()
    elif antwoord1 == "B" or antwoord1 == "b":
        print("je gaat gelijk weg rennen")
        vraag19()

    else:
        print("\nkies A of B")
        vraag4()

def vraag5():  
    print("waar rij je heen \n \nA: naar de grens \nB: naar de haven \nC: naar het vliegveld \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je kwam een paar soldaten tegen en bent nu dood")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je kwam veilig aan bij de haven")
        vraag6()

    elif antwoord1 == "C" or antwoord1 == "c":
        print("het is erg druk op het vliegveld grote mensenmassa belemeren je doorgang")
        vraag10()

    else:
        print("\nkies A B of C")
        vraag5()

def vraag6():  
    print("wil je iemand omkopen voor een plek op een bootje \n \nA: ja \nB: nee \n")
    antwoord1 = input("kies A of B ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je geld is nu op maar je zit op de boot naar een eiland")
        vraag7("antwoord niet mogelijk in jouw situatie")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("via een achteringang heb je een bootje gekaapt en gaat naar een eiland")
        vraag7(" je koopt een vlieg ticket naar Nederland")


    else:
        print("\nkies A of B")
        vraag6()

def vraag7(geldop):  
    print("wat wil je nu doen \n \nA: veder met de bootreis \nB: naar het vluchtelingen kamp  \nC:" + geldop +"\n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je boot was te zwaar beladen en sloeg om en je bent verdronken")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("")
        vraag8()

    elif antwoord1 == "C" or antwoord1 == "c":
        if geldop == " je koopt een vlieg ticket naar Nederland":
            print("je bent veilig in Nederland aangekomen")
            vraag9()
        else:
            print("\nkies A of B")
            vraag7(" antwoord niet mogelijk in jouw situatie")

    else:
        print("\nkies A B of C")
        vraag7(geldop)

def vraag8():  
    print("wat is je volgende stap \n \nA: asiel vragen in Nederland \nB: in het vluchtelingenkamp blijven\nC: naar huis \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je zit in de procedure naar Nederland")
        vraag9()


    elif antwoord1 == "B" or antwoord1 == "b":
        print("je bent de rest van je leven in het vluchtelingenkamp gebleven onder erbarmelijke omstandigheden maar wel gelukkig")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("je bent thuis aangekomen")
        vraag1()

    else:
        print("\nkies A B of C")
        vraag8()

def vraag9():  
    print("wat ga je in Nederland doen \n \nA: de taal leren, een woonruimte zoeken en een baan zoeken \nB: wachten tot de situatie verbeterd in mijn thuisland \nC: weer naar huis gaan \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("dat is gelukt. je hebt nu een fijn en veilig leven")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("5 jaar later kan je weer terug naar huis")
        vraag1()

    elif antwoord1 == "C" or antwoord1 == "c":
        print("je bent veiling thuis aangekomen")
        vraag1()

    else:
        print("\nkies A B of C")
        vraag9()

def vraag10():  
    print("heb je gewerkt voor een europees land \n \nA: ja \nB: nee \n")
    antwoord1 = input("kies A of B ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je gaat op zoek naar de ambasade medewerker")
        vraag11()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je kiest een andere route")
        vraag6()

    else:
        print("\nkies A of B")
        vraag10()

def vraag11():  
    print("heb je de ambasade medewerker gevonden\n \nA: ja \nB: nee \n")
    antwoord1 = input("kies A of B ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je hebt een ticket naar nederland gekregen")
        vraag8()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je kiest een andere route")
        vraag5()

    else:
        print("\nkies A of B")
        vraag11()

def vraag12():  
    print("zijn jullie mobiel \n \nA: we hebben een auto \nB: we hebben een ezel\n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("Jullie stappen snel in de auto")
        vraag13()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je loopt met je ezel naar het station")
        vraag15()

    else:
        print("\nkies A B of C")
        vraag12()

def vraag13():  
    print("waar rijden jullie heen \n \nA: grens \nB: haven \nC: vliegveld \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je gaat naar de grenss")
        vraag14()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("")
        vraag6()

    elif antwoord1 == "C" or antwoord1 == "c":
        print("bent je fammlie kwijt geraakt in de mensenmassa zorg goed voor je zelf")

    else:
        print("\nkies A B of C")
        vraag13()

def vraag14():  
    print("er is een weg afzetting, je moet kiezen tussen links of rechts \n \nA: links \nB: rechts \nC: terug \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je ging over de grens en bent nu veilig")
        vraag8()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("jullie kwam een paar sodaten tegen en gingen dood")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("je gaat terug")
        vraag13()

    else:
        print("\nkies A B of C")
        vraag14()

def vraag15():  
    print("wat is je volgende stap \n \nA: met ezel in de trein \nB: zonder ezel in de trein \nC: te voet veder \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("jullie worden met ezel uit de trein gezet en moet te voet veder en jullie belanden in de woestijn")
        vraag16()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("de trein ging het land uit jullie zijn nu veilig")
        vraag8()

    elif antwoord1 == "C" or antwoord1 == "c":
        print("jullie gaan te voet veder en jullie belanden in de woestijn ")
        vraag16()

    else:
        print("\nkies A B of C")
        vraag15()

def vraag16():  
    print("na dagen lopen word je moeder ziek wat wil je doen \n \nA: laat haar achter \nB: je moeder op de ezel doen \n")
    antwoord1 = input("kies A of B ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je vond water")
        vraag18(0)

    elif antwoord1 == "B" or antwoord1 == "b":
        print("")
        vraag17()

    else:
        print("\nkies A of B")
        vraag16()

def vraag17():  
    print("de ezel is nu moe wat doe je nu\n \nA: laat je moeder achter en neem de ezel met water\nB: laat de ezel achter en draag je moeder \n")
    antwoord1 = input("kies A of B==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("later vond je water en kwam er achter dat je je moeder voor niks had achtergelaten")
        vraag18(0)

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je vond net op tijd water en overleefde")

    else:
        print("\nkies A of B")
        vraag17()

def vraag18(snuf):  
    print("wat wil je nu doen \n \nA: blijf bij het water allen \nB: ga veder in de woestijn\n")
    antwoord1 = input("kies A of B ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je hebt 3 maanden hier gebleefen tot twee aardige mensen je vonden en hiepen")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je verdroog in de woestijn")

    elif antwoord1 == "C" or antwoord1 == "c":
        if snuf == 0:
            print("\nwaarom koos je C???\n")
            vraag18(2)
        elif snuf == 2:
            print("\nwhy??????\n")
            vraag18(3)
        elif snuf == 3:
            print("\nzo ga je niet winnen hoor\n")
            vraag18(4)
        elif snuf == 4:
            print("\nwil je echt zo winnen?\n")
            vraag18(5)
        elif snuf == 5:
            print("\noke jij wint zucht\n")
            time.sleep(3)
            print("ik ga mij zelf nu afsluiten")
            time.sleep(3)
            print("oke doei")
            time.sleep(3)
            exit() 
            

    else:
        print("\nkies A of B")
        vraag18(snuf)

def vraag19():  
    print("je bent aan gekomen in een dorp dicht bij wat wil je doen \n \nA: onderdak zoeken \nB: een auto stelen \n")
    antwoord1 = input("kies A of B ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je hebt een oude schuur gevonden")
        vraag20()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je hebt een auto gestolen")
        vraag5()

    else:
        print("\nkies A of B")
        vraag19()

def vraag20():  
    print("de schuur lekt\n \nA: een andere plek vinden \nB: er niks aan doen\n")
    antwoord1 = input("kies A of B==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je werd gevonden en opgepakt")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je hebt wel oke geslapen ")
        vraag21()

    else:
        print("\nkies A of B")
        vraag20()

def vraag21():  
    print("wat ga je nu doen \n \nA: alsnog een auto stelen \nB: naar een ander dorp\n")
    antwoord1 = input("kies A of B ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je hebt alsnog een auto gestolen")
        vraag5()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("")
        vraag19()

    else:
        print("\nkies A B of C")
        vraag21()

vraag1()

while True:
    print("\nwil je nog een keer spelen")
    vraag0 = input("kies ja of nee ==> ")
    if vraag0 == "ja":
        vraag1()
    elif vraag0 == "nee":
        break
    else:
        print("\ndat is geen andwoord")

