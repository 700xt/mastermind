from random import choice
from sys import exit
from os.path import isfile






nb_tentative = 12


#initialisation des fichiers
if not (isfile("nb_parti.txt")) or not (isfile("score.txt")):
    init()

def init ():
    for file in ["nb_parti.txt","score.txt"]:
        with open(file,'w') as f:
            f.write("0")

def show_score(score,nb_parti):
    ratio_text = ""
    if nb_parti != 0:
        ratio = score/nb_parti
        ratio_text = f"Score moyen {ratio}"
    print (f"Nombre de partie : {nb_parti} \n Score total : {score} \n {ratio_text}")


def game():
    
    #Generation de l'enigme
    first = choice(['R','G','B','Y','P','W'])
    second = choice(['R','G','B','Y','P','W'])
    third = choice(['R','G','B','Y','P','W'])
    four = choice(['R','G','B','Y','P','W'])
    five = choice(['R','G','B','Y','P','W'])
    six = choice(['R','G','B','Y','P','W'])
    
    #initialisation des variables
    first_caract = str()
    second_caract = str()
    third_caract = str()
    four_caract = str()
    five_caract = str()
    six_caract = str()

    #rajouter ou enlever un caractére (min :1 max:6)
    solve = (first+second+third+four)
    print (solve)
    
    stat = {}
    for file in ["nb_parti","score"]:
        with open(file+".txt",'r') as f:
            stat[file] = int(f.read())
    show_score (stat["score"],stat["nb_parti"])
    
    main_menu = input ("Voulez vous jouer (J), Remettre les stat a zero (R), Quittez (Q)  : ")
    main_menu = main_menu.upper ()
    if main_menu == 'R':
        init()
        game()
    elif main_menu == 'J':
        pass
    else:
        exit()


    #Boucle tentative
    a=0
    while a<nb_tentative: 
        print(f"Mastermind => (R)ed, (G)reen, (B)lue, (Y)ellow, (P)urple et (W)hite")
        print("La solution sera sous la forme de 4 inconnu ex rypw pour red yellow purple white.\nSi X apparait => la lettre n'est pas bonne.\nSi Y apparait => La lettre n'est pas a la bonne place")
        combination = input ("Combinaison couleur :")
        combination = combination.upper ()
        c=0
        if combination == solve :
            print("Victoire")
            show_score (stat["score"],stat["nb_parti"])
            stupid = True
            while (stupid):
                again = input ("Voulez vous rejouer O/N : ")
                again = again.upper ()
                if again == 'O':
                    stupid = False
                    for file in ["nb_parti","score"]:
                        with open(file+".txt",'w') as f:
                            f.write (str(stat[file]))
                    game()
                else:
                    stupid = False
                    for file in ["nb_parti","score"]:
                        with open(file+".txt",'w') as f:
                            f.write (str(stat[file]))
                    exit()
            else:
                print ("Veuillez entrer O ou N ")
        for letter in combination:
            if c==0:
                if letter==first:
                    first_caract=first
                elif letter==second:
                    first_caract="Y"
                elif letter==third:
                    first_caract="Y"
                elif letter==four:
                    first_caract="Y"
                else:
                    first_caract="X"
            if c==1:
                if letter==second:
                    second_caract=second
                elif letter==first:
                    second_caract='Y'
                elif letter==third:
                    second_caract="Y"
                elif letter==four:
                    second_caract="Y"
                else:
                    second_caract="X"
            if c==2:
                if letter==third:
                    third_caract=third
                elif letter==first:
                    third_caract="Y"
                elif letter==second:
                    third_caract="Y"    
                elif letter==four:
                    third_caract="Y"
                else:
                    third_caract="X"
            if c==3:
                if letter==four:
                    four_caract=four
                elif letter==first:
                    third_caract="Y"
                elif letter==second:
                    third_caract="Y"
                elif letter==third:
                    third_caract="Y"
                else:
                    four_caract="X"
            
            c+=1
                
        else:
            a += 1
        print(f"{first_caract}{second_caract}{third_caract}{four_caract}{five_caract}{six_caract}")
        del (combination)
        stat["score"] += a
        stat["nb_parti"] += 1
        
    for file in ["nb_parti","score"]:
        with open(file+".txt",'w') as f:
            f.write (str(stat[file]))
    show_score (stat["score"],stat["nb_parti"])    
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


