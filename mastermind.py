from random import choice
from sys import exit

#Generation de chaine de caractere
first = choice(['R','G','B','Y','P','W'])
second = choice(['R','G','B','Y','P','W'])
third = choice(['R','G','B','Y','P','W'])
four = choice(['R','G','B','Y','P','W'])
solve = (first+second+third+four)
print (solve)
b=12
fi_caract = str()
se_caract = str()
th_caract = str()
fo_caract = str()
nb_tentative = 12


#Boucle tentative
a=0
while a<nb_tentative: 
    print(f"Mastermind => (R)ed, (G)reen, (B)lue, (Y)ellow, (P)urple et (W)hite")
    input("La solution sera sous forme YRZZ pour Y: mauvaise endroit")
    combination = input ("Combinaison couleur sous forme rywp:")
    combination = combination.upper ()
    c=0
    if combination == solve :
        print("Victoire")
        print(f"score : {score} ")
        exit()
    for letter in combination:
        if c==0:
            if letter==first:
                fi_caract=first
            elif letter==second:
                fi_caract="X"
            elif letter==third:
                fi_caract="X"
            elif letter==four:
                fi_caract="X"
            else:
                fi_caract=" "
        if c==1:
            if letter==second:
                se_caract=second
            elif letter==first:
                se_caract="X"
            elif letter==third:
                se_caract="X"
            elif letter==four:
                se_caract="X"
            else:
                se_caract=" "
        if c==2:
            if letter==third:
                th_caract=third
            elif letter==first:
                th_caract="X"
            elif letter==second:
                th_caract="X"
            elif letter==four:
                th_caract="X"
            else:
                th_caract=" "
        if c==3:
            if letter==four:
                fo_caract=four
            elif letter==first:
                fo_caract="X"
            elif letter==second:
                fo_caract="X"
            elif letter==third:
                fo_caract="X"
            else:
                fo_caract=" "
        c+=1
        
    else:
        a+=1
        score=b-a
    print(f"{fi_caract}{se_caract}{th_caract}{fo_caract}")

exit()



print("Tentative épuisé")
        

# first_color = input ("Choix pour la premiére couleur :")
# first_color = first_color.upper ()
# second_color = input ("Choix pour la deuxiéme couleur :")
# second_color = second_color.upper ()
# third_color = input ("Choix pour la troisiéme couleur :")
# third_color = third_color.upper ()
# four_color = input ("Choix pour la quatriéme couleur :")
# four_color = four_color.upper ()

#if first_color == 'R,G,B,Y,P,W':


