from random import choice
from sys import exit


def game():
    #Generation de chaine de caractere
    first = choice(['R','G','B','Y','P','W'])
    second = choice(['R','G','B','Y','P','W'])
    third = choice(['R','G','B','Y','P','W'])
    four = choice(['R','G','B','Y','P','W'])
    five = choice(['R','G','B','Y','P','W'])
    six = choice(['R','G','B','Y','P','W'])

    #rajouter ou enlever un caractére (min :1 max:6)
    solve = (first+second+third+four)
    print (solve)

    first_caract = str()
    second_caract = str()
    third_caract = str()
    four_caract = str()
    five_caract = str()
    six_caract = str()
    nb_tentative = 12





    
    #Boucle tentative
    a=0
    while a<nb_tentative: 
        print(f"Mastermind => (R)ed, (G)reen, (B)lue, (Y)ellow, (P)urple et (W)hite")
        print("La solution sera sous la forme de 4 inconnu ex rypw pour red yellow purple white\n")
        combination = input ("Combinaison couleur :")
        combination = combination.upper ()
        print (combination)
        c=0
        if combination == solve :
            print("Victoire")
            print(f"score : {score} ")
            exit()
        for letter in combination:
            if c==0:
                if letter==first:
                    first_caract=first
                elif letter==second:
                    first_caract="X"
                elif letter==third:
                    first_caract="X"
                elif letter==four:
                    first_caract="X"
                elif letter==five:
                    first_caract='X'
                elif letter==six:
                    first_caract='X'
                else:
                    first_caract=" "
            if c==1:
                if letter==second:
                    second_caract=second
                elif letter==fisrt:
                    second_caract='X'
                elif letter==third:
                    second_caract="X"
                elif letter==four:
                    second_caract="X"
                elif letter==five:
                    second_caract="X"
                elif letter==six:
                    second_caract='X'
                else:
                    second_caract=" "
            if c==2:
                if letter==third:
                    third_caract=third
                elif letter==first:
                    third_caract="X"
                elif letter==second:
                    third_caract="X"    
                elif letter==four:
                    third_caract="X"
                elif letter==five:
                    third_caract="X"
                elif letter==six:
                    third_caract="X"
                else:
                    third_caract=" "
            if c==3:
                if letter==four:
                    four_caract=four
                elif letter==first:
                    third_caract="X"
                elif letter==second:
                    third_caract="X"
                elif letter==third:
                    third_caract="X"
                elif letter==five:
                    four_caract="X"
                elif letter==six:
                    four_caract="X"
                else:
                    four_caract=" "
            if c==4:
                if letter==five:
                    five_caract=five
                elif letter==first:
                    five_caract="X"
                elif letter==second:
                    five_caract="X"
                elif letter==third:
                    five_caract="X"
                elif letter==four:
                    five_caract="X"
                elif letter==six:
                    five_caract="X"
                else:
                    five_carac=" "
            if c==5:
                if letter==six:
                    six_caract=six
                elif letter==first:
                    six_caract="X"
                elif letter==second:
                    six_caract="X"
                elif letter==third:
                    six_caract="X"
                elif letter==four:
                    six_caract="X"
                elif letter==five:
                    six_caract="X"
                else:
                    six_carac=" "
            c+=1
                
        else:
            a+=1
            score=nb_tentative-a
        print(f"{first_caract}{second_caract}{third_caract}{four_caract}{five_caract}{six_caract}")
        print(f"tentative restante : {score}")
    stupid = True
    while (stupid):
        again = input ("Voulez vous rejouer O/N : ")
        again = again.upper ()
        if again == 'O':
            stupid = False
            game()
        elif again == 'N':
            stupid = False       
        else:
            print ("Veuillez entrer O ou N ")
game()


