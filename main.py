import random
import time

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 10

    def attack(self, other, attack_type):
        if attack_type == "coup rapide":
            damage = 1
            print(f"{self.name} utilise un coup rapide sur {other.name}!")
        elif attack_type == "coup puissant":
            damage = 2
            print(f"{self.name} utilise un coup puissant sur {other.name}!")
        elif attack_type == "coup critique":
            damage = 3
            print(f"{self.name} utilise un coup critique sur {other.name}!")
        else:
            print(f"{self.name} hésite et ne fait rien!")
            damage = 0
        
        other.hp -= damage
        if damage > 0:
            print(f"{other.name} perd {damage} HP! Il reste {other.hp} HP à {other.name}.")
        
        if other.hp <= 0:
            print(f"{other.name} est mort!")

def choose_attack():
    print("Choisissez une attaque :")
    print("1 - Coup rapide (1 HP de dégâts)")
    print("2 - Coup puissant (2 HP de dégâts)")
    print("3 - Coup critique (3 HP de dégâts)")
    
    choice = input("Votre choix : ")
    if choice == "1":
        return "coup rapide"
    elif choice == "2":
        return "coup puissant"
    elif choice == "3":
        return "coup critique"
    else:
        print("Choix invalide, aucun coup n'a été porté.")
        return "rien"

def battle(player1, player2):
    while player1.hp > 0 and player2.hp > 0:
        print(f"\n{player1.name} (HP: {player1.hp}) VS {player2.name} (HP: {player2.hp})")
        
        print(f"\nC'est au tour de {player1.name}!")
        attack_type = choose_attack()
        player1.attack(player2, attack_type)
        if player2.hp <= 0:
            break

        print(f"\nC'est au tour de {player2.name}!")
        attack_type = choose_attack()
        player2.attack(player1, attack_type)
        time.sleep(1)

    print("Le combat est terminé.")

def main():
    print("Bienvenue dans le RPG console!")
    player1_name = input("Entrez le nom du premier personnage: ")
    player2_name = input("Entrez le nom du deuxième personnage: ")
    
    player1 = Character(player1_name)
    player2 = Character(player2_name)
    
    battle(player1, player2)
    
    input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()
