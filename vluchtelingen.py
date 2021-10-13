
print()
def vraag1():  
    print()
    print("vraag1 \n \nA: antwoord \nB: antwoord \nC: antwoord \n")
    antwoord1 = input("kies A B of C ==> ")
    
    if antwoord1 == "A" or antwoord1 == "a":
        print("A")

    elif antwoord1 == "B" or antwoord1 == "b":
        print("B")

    elif antwoord1 == "C" or antwoord1 == "c":
        print("C")
    
    else:
        print()
        print("kies A B of C")
        print()
        vraag1()


vraag1()