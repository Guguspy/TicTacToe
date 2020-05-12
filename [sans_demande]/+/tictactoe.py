import time
import emoji


class Wipe(object):
    def __repr__(self):
        return '\n'*40
wipe = Wipe()
print(wipe)

case=''
case1='a'
case2='b'
case3='c'
case4='d'
case5='e'
case6='f'
case7='g'
case8='h'
case9='i'

a=case1
b=case2
c=case3
d=case4
e=case5
f=case6
g=case7
h=case8
i=case9

choix=''


rien=''

nom=''
J1=''
J2=''

x='X'
o='O'

cross=x
circle=o

wincross=cross+cross+cross
wincircle=circle+circle+circle

valid=''
jeu=0




tour=0



def grille(): #on initialise la grille du morpion
  print('\n\n        ',case1,'|',case2,'|',case3,'\n        -----------\n        ',case4,'|',case5,'|',case6,'      Tic ° Tac ° Toe | by Gugus\n        -----------\n        ',case7,'|',case8,'|',case9,'\n')


def finish(): #on initialise le "départ"
    print('\n\n  Partie terminée !\n\n  Merci d\'avoir joué !')
    time.sleep(8)
    quit()


def win(): #Régle de victoire
            
        #Honrizontal J1
        if case1 + case2 + case3 == wincross:              # si toutes les cases sont marqué par un X, elles seront alors égual à wincross, qui est lui défini par 'XXX'
            grille()
            print('\n\n        ',J1,' win à l\'honrizontal en 1ère ligne !')
            time.sleep(2)
            finish()

        elif case4 + case5 + case6 == wincross:
            grille()
            print('\n\n        ',J1,' win à l\'honrizontal en 2nd ligne !')
            finish()

        elif case7 + case8 + case9 == wincross:
            grille()
            print('\n\n        ',J1,' win à l\'honrizontal en 3ème ligne !')
            finish()


        #Honrizontal J2    
        elif case1 + case2 + case3 == wincircle:           # si toutes les cases sont marqué par un O, elles seront alors égual à wincircle, qui est lui défini par 'OOO'
            grille()
            print('\n\n        ',J2,' win à l\'honrizontal en 1ère ligne !')
            finish()
            
        elif case4 + case5 + case6 == wincircle:
            grille()
            print('\n\n        ',J2,' win à l\'honrizontal en 2nd ligne !')
            finish()

        elif case7 + case8 + case9 == wincircle:
            grille()
            print('\n\n        ',J2,' win à l\'honrizontal en3ème ligne !')
            finish()


        #Vertical J1
        elif case1 + case4 + case7 == wincross:           # si toutes les cases sont marqué par un X, elles seront alors égual à wincross, qui est lui défini par 'XXX'
            grille()
            print('\n\n        ',J1,' win à la vertical en 1ère colonne !')
            finish()

        elif case2 + case5 + case8 == wincross:
            grille()
            print('\n\n        ',J1,' win à la vertical en 2nd colonne !')
            finish()

        elif case3 + case6 + case9 == wincross:
            grille()
            print('\n\n        ',J1,' win à la vertical en 3ème colonne !')
            finish()

            
        #Vertical J2
        elif case1 + case4 + case7 == wincircle:          # si toutes les cases sont marqué par un O, elles seront alors égual à wincircle, qui est lui défini par 'OOO'
            grille()
            print('\n\n        ',J2,' win à la vertical en 1ère colonne !')
            finish()

        elif case2 + case5 + case8 == wincircle:
            grille()
            print('\n\n        ',J2,' win à la vertical en 2nd colonne !')
            finish()

        elif case3 + case6 + case9 == wincircle:
            grille()
            print('\n\n        ',J2,' win à la vertical en 3ème colonne !')
            finish()


        #Diagonale C1 > C9 J1                             # si toutes les cases sont marqué par un X, elles seront alors égual à wincross, qui est lui défini par 'XXX'
        elif case1 + case5 + case9 == wincross:
            grille()
            print('\n\n        ',J1,' win à la diagonale !')
            finish()


        #Diagonale C1 > C9 J2                             # si toutes les cases sont marqué par un O, elles seront alors égual à wincircle, qui est lui défini par 'OOO'
        elif case1 + case5 + case9 == wincircle:
            grille()
            print('\n\n        ',J2,' win à la diagonale !')
            finish()

        #Diagonale C3 > C7 J1                             # si toutes les cases sont marqué par un X, elles seront alors égual à wincross, qui est lui défini par 'XXX'
        elif case3 + case5 + case7 == wincross:
            grille()
            print('\n\n        ',J1,' win à la diagonale !')
            finish()

        #Diagonale C3 > C7 J2                             # si toutes les cases sont marqué par un O, elles seront alors égual à wincircle, qui est lui défini par 'OOO'
        elif case3 + case5 + case7 == wincircle:
            grille()
            print('\n\n        ',J2,' win à la diagonale !')
            finish()



##while nom==rien :
##    print(wipe)
##    print('  Voulez vous choisir vos noms ?\n')
##    nom = input('  [Oui ou Non] >  ') #on fait choisir à l'user si il veut ou non, enregistrer un nom pour les joueurs
##    nom=nom.lower()#on transforme le texte récupérer en minuscule, pour eviter de créé trop de combinaison, la réponse sera soit oui, soit non, soit 'autres'
##    if nom == 'oui':# si oui, les joueurs choisiront les pseudos
##        while J1==rien : #si l'utilisateur se trompe, il pourra reformuler sa réponse
##            print('\n  Choisir le nom de Joueur 1 :')
##            J1=input('     >  ')
##            print('')
##            if J1!=rien : #on vérifie que J1 n'est pas vide
##                print('  Joueur 1 se nommera :',J1)
##                time.sleep(0.5)
##            else:
##                print('\n  Le champ du nom ne peut pas être vide\n')
##                J1=rien
##                
##        while J2==rien:
##            print('\n  Choisir le nom de Joueur 2 :')
##            J2=input('     >  ')
##            print('')
##            if J2!=rien : #pareil que J1 mais pour J2
##                print('  Joueur 2 se nommera :',J2)
##                time.sleep(0.5)
##            else:
##                print('\n  Le champ du nom ne peut pas être vide\n')
##                J2=rien
##                
##        print('\n  Place aux consignes maintenant !\n')
##        time.sleep(3)
##        
##    elif nom == 'non':#si non, les joueurs auront J1 et J2 par défaut, comme nom
##        print('\n\n\n  Vous porterez les noms de J1 et J2.\n')
##        J1='J1'
##        J2='J2'
##        time.sleep(1)
##        print('\n  Place aux consignes maintenant !\n')
##        time.sleep(2.5)
##    else:
##        print('\n\n  Veuillez choisir entre \'Oui\' ou \'Non\' !\n') #choix autre que oui ou non, on repose la question grâce au while
##        time.sleep(2.5)
##        nom=''
##
##        
##
##while valid==rien : # si l'utilisateur se trompe, il pourra reformuler sa réponse
##    print(wipe)
##    print('  Tic Tac Toe / Morpion')
##    time.sleep(0.2)
##    print('')
##    print('  La grille sera présenté sous cette forme :')
##    time.sleep(0.2)
##    grille() #On affiche la grille
##    time.sleep(0.2)
##    print('\n  Il vous suffira de choisir le numéro de la case,')
##    time.sleep(0.2)
##    print('  pour le remplacer soit par un ',cross,' soit par un ',circle,'.\n')
##    time.sleep(0.2)
##    print('\n ',J1,'aura les',cross,' | ',J2,'aura les',circle,'!\n')
##    time.sleep(0.2)
##    print('  Êtes-vous prêt à jouer ? \n')
##    time.sleep(0.2)
##    valid = input('     [Oui ou Non] >  ') # même système que pour les pseudos
##    valid=valid.lower()
##    if valid == 'oui':
##        print('\n\n\n  Alors passons maintenant au Jeu !\n')
##        time.sleep(3)
##        jeu=1
##    elif valid == 'non':
##        print('\n\n  Les consignes vont être répété.\n')
##        time.sleep(3)
##        valid=''
##        print(wipe)
##    else:
##        print('\n  Veuillez choisir entre \'Oui\' ou \'Non\' !\n')
##        time.sleep(2)
##        valid=''
##        print(wipe)




J1='J1'
J2='J2'

z=0        #<- Pour patch
while z==0: #<- une erreur 
    z=1    #<- d'indentation
    #Tour 1
    print(wipe)
    print('')
    print(J1,'commence, veuillez choisir une case :')
    print('\n Tour 1')
    grille() #on affiche la grille
    while choix == rien:
        choix=input('[a-i] > ')  #Pas besoin de vérifier si la case est prise,  c'est le premier tour
        if choix == a:
            case1=cross
            tour=1               #on incrément le nombre de tour (manuellement), pour que les tours se suivent, et qu'il n'y est pas d'erreur.
        elif choix == b:
            case2=cross
            tour=1
        elif choix == c:
            case3=cross
            tour=1
        elif choix == d:
            case4=cross
            tour=1
        elif choix == e:
            case5=cross
            tour=1
        elif choix == f:
            case6=cross
            tour=1
        elif choix == g:
            case7=cross
            tour=1
        elif choix == h:
            case8=cross
            tour=1
        elif choix == i:
            case9=cross
            tour=1
        else:
            print('\nchoix invalide\n\n') #Erreur si choix !=a/b/c/d/e/f/g/h/i
            choix=''




    #Tour 2

    
    if tour ==1:
        print(wipe)
        print('\n\n',J2,' c\'est à toi !')
        print('\n Tour 2')
        grille()
        choix=''
        while choix ==rien:
            choix=input('[a-i] > ') 
            if choix == a:                               #On vérifie que le choix sélectioner par le J2
                if case1 == cross and circle:            #n'est pas le même que le J1 et on gardera cette
                    print('\nchoix invalide\n\n')        #méthode pour la suite
                    choix=''
                else:
                    case1=circle
                    win()                                # On initialise la def win(), pour vérifier si il y a victoire, même si inutile dans les 4 premiers tours.
                    tour=2
                    
            elif choix == b:
                if case2 == cross and circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case2=circle
                    win()
                    tour=2

            elif choix == c:
                if case3 == cross and circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case3=circle
                    win()
                    tour=2
                    
            elif choix == d:
                if case4 == cross and circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case4=circle
                    win()
                    tour=2

            elif choix == e:
                if case5 == cross and circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case5=circle
                    win()
                    tour=2

            elif choix == f:
                if case6 == cross and circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case6=circle
                    win()
                    tour=2

            elif choix == g:
                if case7 == cross and circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case7=circle
                    win()
                    tour=2

            elif choix == h:
                if case8 == cross and circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case8=circle
                    win()
                    tour=2

            elif choix == i:
                if case9 == cross and circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case9=circle
                    win()
                    tour=2

            else:
                print('\nchoix invalide\n\n')
                choix=''




    #Tour 3

    if tour ==2:
        print(wipe)
        print('\n\n',J1,' c\'est à toi !')
        print('\n Tour 3')
        grille()
        choix=''
        while choix ==rien:
            choix=input('[a-i] > ')
            if choix == a:
                if case1 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case1 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case1=cross
                    win()
                    tour=3
                    
            elif choix == b:
                if case2 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case2 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case2=cross
                    win()
                    tour=3

            elif choix == c:
                if case3 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case3 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case3=cross
                    win()
                    tour=3
                    
            elif choix == d:
                if case4 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case4 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case4=cross
                    win()
                    tour=3

            elif choix == e:
                if case5 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case5 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case5=cross
                    win()
                    tour=3

            elif choix == f:
                if case6 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case6 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case6=cross
                    win()
                    tour=3

            elif choix == g:
                if case7 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case7 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case7=cross
                    win()
                    tour=3

            elif choix == h:
                if case8 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case8 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case8=cross
                    win()
                    tour=3

            elif choix == i:
                if case9 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case9 == circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case9=cross
                    win()
                    tour=3

            else:
                print('\nchoix invalide\n\n')
                choix=''



    #Tour 4


    if tour ==3:
        print(wipe)
        print('\n\n',J2,' c\'est à toi !')
        print('\n Tour 4')
        grille()
        choix=''
        while choix ==rien:
            choix=input('[a-i] > ')
            if choix == a:
                if case1 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case1 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case1=circle
                    win()
                    tour=4
                    
            elif choix == b:
                if case2 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case2 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case2=circle
                    win()
                    tour=4

            elif choix == c:
                if case3 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case3 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case3=circle
                    win()
                    tour=4
                    
            elif choix == d:
                if case4 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case4 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case4=circle
                    win()
                    tour=4

            elif choix == e:
                if case5 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case5 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case5=circle
                    win()
                    tour=4

            elif choix == f:
                if case6 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case6 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case6=circle
                    win()
                    tour=4

            elif choix == g:
                if case7 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case7 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case7=circle
                    win()
                    tour=4

            elif choix == h:
                if case8 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case8 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case8=circle
                    win()
                    tour=4

            elif choix == i:
                if case9 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case9 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case9=circle
                    win()
                    tour=4

            else:
                print('\nchoix invalide\n\n')
                choix=''



    #Tour 5


    if tour ==4:
        print(wipe)
        print('\n\n',J1,' c\'est à toi !')
        print('\n Tour 5')
        grille()
        choix=''
        while choix ==rien:
            choix=input('[a-i] > ')
            if choix == a:
                if case3 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case3 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case1=cross
                    win()
                    tour=5
                    
            elif choix == b:
                if case3 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case3 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case2=cross
                    win()
                    tour=5

            elif choix == c:
                if case3 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case3 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case3=cross
                    win()
                    tour=5
                    
            elif choix == d:
                if case4 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case4 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case4=cross
                    win()
                    tour=5

            elif choix == e:
                if case5 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case5 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case5=cross
                    win()
                    tour=5

            elif choix == f:
                if case6 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case6 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case6=cross
                    win()
                    tour=5

            elif choix == g:
                if case7 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case7 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case7=cross
                    win()
                    tour=5

            elif choix == h:
                if case8 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case8 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case8=cross
                    win()
                    tour=5

            elif choix == i:
                if case9 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case9 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case9=cross
                    win()
                    tour=5
                    
                    

            else:
                print('\nchoix invalide\n\n')
                choix=''



    #Tour 6

    if tour ==5:
        print(wipe)
        print('\n\n',J2,' c\'est à toi !')
        print('\n Tour 6')
        grille()
        choix=''
        while choix ==rien:
            choix=input('[a-i] > ')
            if choix == a:
                if case1 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case1 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case1=circle
                    win()
                    tour=6
                    
            elif choix == b:
                if case2 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case2 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case2=circle
                    win()
                    tour=6

            elif choix == c:
                if case3 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case3 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case3=circle
                    win()
                    tour=6
                    
            elif choix == d:
                if case4 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case4 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case4=circle
                    win()
                    tour=6

            elif choix == e:
                if case5 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case5 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case5=circle
                    win()
                    tour=6

            elif choix == f:
                if case6 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case6 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case6=circle
                    win()
                    tour=6

            elif choix == g:
                if case7 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case7 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case7=circle
                    tour=6

            elif choix == h:
                if case8 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case8 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case8=circle
                    win()
                    tour=6

            elif choix == i:
                if case9 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case9 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case9=circle
                    win()
                    tour=6

            else:
                print('\nchoix invalide\n\n')
                choix=''

    #Tour 7
    if tour ==6:
        print(wipe)
        print('\n\n',J1,' c\'est à toi !')
        print('\n Tour 7')
        grille()
        choix=''
        while choix ==rien:
            choix=input('[a-i] > ')
            if choix == a:
                if case1 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case1 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case1=cross
                    win()
                    tour=7
                    
            elif choix == b:
                if case2 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case2 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case2=cross
                    win()
                    tour=7

            elif choix == c:
                if case3 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case3 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case3=cross
                    win()
                    tour=7
                    
            elif choix == d:
                if case4 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case4 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case4=cross
                    win()
                    tour=7

            elif choix == e:
                if case5 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case5 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case5=cross
                    win()
                    tour=7

            elif choix == f:
                if case6 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case6 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case6=cross
                    win()
                    tour=7

            elif choix == g:
                if case7 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case7 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case7=cross
                    win()
                    tour=7

            elif choix == h:
                if case8 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case8 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case8=cross
                    win()
                    tour=7

            elif choix == i:
                if case9 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case9 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case9=cross
                    win()
                    tour=7
                    
                    
            else:
                print('\nchoix invalide\n\n')
                choix=''


    #Tour 8
    if tour ==7:
        print(wipe)
        print('\n\n',J2,' c\'est à toi !')
        print('\n Tour 8')
        grille()
        choix=''
        while choix ==rien:
            choix=input('[a-i] > ')
            if choix == a:
                if case2 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case2 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case1=circle
                    win()
                    tour=8
                    
            elif choix == b:
                if case2 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case2 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case2=circle
                    win()
                    tour=8

            elif choix == c:
                if case3 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case3 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case3=circle
                    win()
                    tour=8
                    
            elif choix == d:
                if case4 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case4 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case4=circle
                    win()
                    tour=8

            elif choix == e:
                if case5 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case5 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case5=circle
                    win()
                    tour=8

            elif choix == f:
                if case6 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case6 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case6=circle
                    win()
                    tour=8

            elif choix == g:
                if case7 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case7 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case7=circle
                    win()
                    tour=8

            elif choix == h:
                if case8 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case8 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case8=circle
                    win()
                    tour=8

            elif choix == i:
                if case9 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case9 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case9=circle
                    win()
                    tour=8

            else:
                print('\nchoix invalide\n\n')
                choix=''

    #Tour 9
    if tour ==8:
        print(wipe)
        print('\n\n',J1,' c\'est à toi !')
        print('\n Tour 9')
        grille()
        choix=''
        while choix ==rien:
            choix=input('[a-i] > ')
            if choix == a:
                if case1 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case1 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case1=cross
                    win()
                    tour=9
                    
            elif choix == b:
                if case2 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case2 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case2=cross
                    win()
                    tour=9

            elif choix == c:
                if case3 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case3 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case3=cross
                    win()
                    tour=9
                    
            elif choix == d:
                if case4 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case4 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case4=cross
                    win()
                    tour=9

            elif choix == e:
                if case5 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case5 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case5=cross
                    win()
                    tour=9

            elif choix == f:
                if case6 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case6 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case6=cross
                    win()
                    tour=9

            elif choix == g:
                if case7 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case7 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case7=cross
                    win()
                    tour=9

            elif choix == h:
                if case8 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case8 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case8=cross
                    win()
                    tour=9

            elif choix == i:
                if case9 == cross :
                    print('\nchoix invalide\n\n')
                    choix=''
                elif case9 ==circle:
                    print('\nchoix invalide\n\n')
                    choix=''
                else:
                    case9=cross
                    win()
                    tour=9
                    
                    
            else:
                print('\nchoix invalide\n\n')
                choix=''


#Draw
if tour ==9: # en cas de non victoire, un draw (équalité) est "deviné"
    print(wipe)
    grille()
    print('\n Égalité !\n')
    time.sleep(5)
    finish()






