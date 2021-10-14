import random 
import time
print()

def vraag1():

    print("\nIs er onrust in jou land? \n \nA: ja: grote onrust \nB: ja: het rommelt een beetje \nC: nee \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("")
        vraag2()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("Wat fijn voor je, je bent veilig")

    else:
        print("\nkies A B of C")
        vraag1()

def vraag2():
    print("\nzou je willen vluchten \n \nA: ja graag zo snel mogelijk \nB: misschien \nC: nee \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je gaat nu naar buiten")
        vraag3()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("")

    else:
        print("\nkies A B of C")
        vraag2()

def vraag3():  
    print("ben je alleen of ben je met meerdere personen \n \nA: ik ben alleen \nB: samen met mijn ouders \nC: met mijn gezin \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je pakt hoogstnoodzakelijke spullen")
        vraag4()

    elif antwoord1 == "B" or antwoord1 == "b":
        print("je sleurt je ouders mee")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("")

    else:
        print("\nkies A B of C")
        vraag3()

def vraag4():  
    print("ben je mobiel \n \nA: ja ik heb een auto \nB: ja ik heb een rugzak \nC: nee \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je stopt de spullen in je auto en rijdt weg")
        vraag5()
    elif antwoord1 == "B" or antwoord1 == "b":
        print("")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("")

    else:
        print("\nkies A B of C")
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
        print("C")

    else:
        print("\nkies A B of C")
        vraag5()

def vraag6():  
    print("wil je iemand omkopen voor een plek op een bootje \n \nA: ja \nB: nee \n")
    antwoord1 = input("kies A of B ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("je geld is nu op maar je zit op de boot naar een eiland")
        vraag7(" antwoord niet mogelijk in jouw situatie")

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
        vraag7()

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
    print("vraag10 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag10()

def vraag11():  
    print("vraag11 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag11()

def vraag12():  
    print("vraag12 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag12()

def vraag13():  
    print("vraag13 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag13()

def vraag14():  
    print("vraag14 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag14()

def vraag15():  
    print("vraag15 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag15()

def vraag16():  
    print("vraag16 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag16()

def vraag17():  
    print("vraag17 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag17()

def vraag18():  
    print("vraag18 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag18()

def vraag19():  
    print("vraag19 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag19()

def vraag20():  
    print("vraag20 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag20()

def vraag21():  
    print("vraag21 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag21()

def vraag22(): 
    print("vraag22 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")

    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")

    else:
        print("\nkies A B of C")
        vraag22()

vraag1()