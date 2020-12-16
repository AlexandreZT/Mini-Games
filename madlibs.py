from os import system

def mad_libs():
    system('cls')
    nb = 12
    print('\nWelcome into the MAD LIBS GAME !')
    txt8 = input("\n13 input needed\nnoun : ")
    txt12= input("\n12 input needed\nadjective : ")
    txt5 = input("\n11 input needed\nnoun : ")
    txt2 = input("\n10 input needed\nsport noun : ")
    txt13 = input("\n9 input needed\nnoun : ")
    txt3 = input("\n8 input needed\ncity name : ")
    txt11 = input("\n7 input needed\nnoun : ")
    txt6 = input("\n6 input needed\naction verb : ")
    txt7 = input("\n5 input needed\nnoun : ")
    txt1 = input("\n4 input needed\nadjective : ")
    txt9 = input("\n3 input needed\nnoun : ")
    txt10 = input("\n2 input needed\nadjective : ")
    txt4 = input("\n1 input needed\nnoun : ")
    
    print("\nOne day my "+txt1+" friend and I decided to go to the "+txt2+" game in "+txt3+".")
    print("We really wanted to see the "+txt4+" play the "+txt5+".")
    print("So we "+txt6+" our "+txt7+" down to the "+txt8+" and bought some "+txt9+".")
    print("We got into the game and it was a lot of fun.")
    print("We ate some "+txt10+" "+txt11+" and drank some "+txt12+" "+txt13+".")
    print("We had a great time! We plan to go again next year!")

if __name__ == "__main__":
    mad_libs()