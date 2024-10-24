import unittest
from main import Character  

class TestRPGGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Character("Joueur1")
        self.player2 = Character("Joueur2")

    def test_character_initialization(self):
        self.assertEqual(self.player1.name, "Joueur1")
        self.assertEqual(self.player2.name, "Joueur2")
        self.assertEqual(self.player1.hp, 10)
        self.assertEqual(self.player2.hp, 10)

    def test_attack(self):
        self.player1.attack(self.player2, "coup rapide")
        self.assertEqual(self.player2.hp, 9) 

        self.player1.attack(self.player2, "coup puissant")
        self.assertEqual(self.player2.hp, 7) 

        self.player1.attack(self.player2, "coup critique")
        self.assertEqual(self.player2.hp, 4) 

        self.player1.attack(self.player2, "mauvaise attaque")
        self.assertEqual(self.player2.hp, 4)  

    def test_death(self):
        self.player1.attack(self.player2, "coup critique") 
        self.player1.attack(self.player2, "coup critique")  
        self.player1.attack(self.player2, "coup critique")  
        self.player1.attack(self.player2, "coup rapide")   
        self.assertEqual(self.player2.hp, 0)
        self.assertEqual(self.player2.hp <= 0, True)  

if __name__ == "__main__":
    unittest.main()
