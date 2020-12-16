from random import randrange
from os import system

def rock_paper_scissors(player, computer): 
    system('cls')
    print('Joueur : ', player, 'Ordinateur : ', computer)
    print("Jeu :\nRésultat :")
    while player != 3 and computer != 3:
        computer_turn = randrange(3)+1 # 1 - 2 ou 3
        try:
            player_turn = eval(input("""
Pour faire pierre tappe 1
Pour faire papier tappe 2
Pour faire ciseaux tappe 3
: """))   
        except:
            rock_paper_scissors(player, computer)

        if player_turn != 1 and player_turn != 2 and player_turn != 3:
            rock_paper_scissors(player, computer)

        if player_turn == 1 and  computer_turn == 1:
            system('cls')
            print('Joueur : ', player, 'Ordinateur : ', computer)
            print("Jeu : Pierre contre Pierre")
            print("Résultat : Égalité")
        
        elif player_turn == 1 and computer_turn == 2:
            system('cls')
            computer+=1
            print('Joueur : ', player, 'Ordinateur : ', computer)
            print("Jeu : Pierre contre Feuille")
            print("Résultat : L'ordinateur gagne la manche")
            

        elif player_turn == 1 and computer_turn == 3:
            system('cls')
            player+=1
            print('Joueur : ', player, 'Ordinateur : ', computer)
            print("Jeu : Pierre contre Ciseaux")
            print("Résultat : Tu gagnes la manche")
        
        elif player_turn == 2 and computer_turn == 1:
            system('cls')
            player+=1
            print('Joueur : ', player, 'Ordinateur : ', computer)
            print("Jeu : Feuille contre Pierre")
            print("Résultat : Tu gagnes la manche")

        elif player_turn == 2 and computer_turn == 2:
            system('cls')
            print('Joueur : ', player, 'Ordinateur : ', computer)
            print("Jeu : Feuille contre Feuille")
            print("Résultat : Égalité")
        
        elif player_turn == 2 and computer_turn == 3:
            system('cls')
            computer+=1
            print('Joueur : ', player, 'Ordinateur : ', computer)
            print("Jeu : Feuille contre Ciseaux")
            print("Résultat : L'ordinateur gagne la manche")
        
        elif player_turn == 3 and computer_turn == 1:          
            system('cls')
            computer+=1
            print('Joueur : ', player, 'Ordinateur : ', computer)
            print("Jeu : Ciseaux contre Pierre")
            print("Résultat : L'ordinateur gagne la manche")

        elif player_turn == 3 and computer_turn == 2:
            system('cls')
            player+=1
            print('Joueur : ', player, 'Ordinateur : ', computer)
            print("Jeu : Ciseaux contre Feuille")
            print("Résultat : Tu gagnes la manche")
            
        
        elif player_turn == 3 and computer_turn == 3:
            system('cls')
            print('Joueur : ', player, 'Ordinateur : ', computer)
            print("Jeu : Ciseaux contre Ciseaux")
            print("Résultat : Égalité")

        if player == 3:
            system('cls')
            print("Tu as a gagné!")
            break

        elif computer ==3:
            system('cls')
            print("L'ordinateur a gagné!")
            break
    
if __name__ == "__main__":   
    rock_paper_scissors(0, 0)  