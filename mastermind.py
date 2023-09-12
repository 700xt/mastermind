from random import choice

#Generation de chaine de caractere
first = choice(['R','G','B','Y','P','W'])
second = choice(['R','G','B','Y','P','W'])
third = choice(['R','G','B','Y','P','W'])
four = choice(['R','G','B','Y','P','W'])
solve = (first+second+third+four)
print (solve)





#Boucle tentative
a=0
while a<12:
    print(f"Mastermind => Rappel des couleurs disponible :(R)ed, (G)reen, (B)lue, (Y)ellow, (P)urple et (W)hite")
    combination = input ("Combinaison couleur :")
    combination = combination.upper ()
    b=0
    for i in combination:
        print ("i vaut", i)
    if combination == solve :
        print("Victoire")
    else:
        print("Essaye encore")
        a+=1

    print(i)



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


