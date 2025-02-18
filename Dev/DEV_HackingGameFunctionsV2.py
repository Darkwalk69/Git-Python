from os import system, name
from art import tprint
import random

class Player:
    def __init__(self):
        self.inventory = []
        self.balance = 0
        self.detection_chance = 5
        self.counter = 0
        self.stellar_solutions_contract_accepted = False
        
    def check_balance(self):
        return f"Your current balance is: ${self.balance}"
    
    def update_balance(self, amount):
        self.balance += amount
        return self.balance
    
    def show_inventory(self):
        if self.inventory:
            print("--- Your Inventory ---")
            print(f"Balance: ${self.balance}\n")
            for item in self.inventory:
                print(item)
        else:
            print("Your inventory is empty.")
            

class HackingGames:
    def __init__(self, player):
        self.player = player
        self.game_functions = GameFunctions(player)
        self.HackingGames = {
            "1": self.PasswordCracker,
            "2": self.DataExtraction,
            "3": self.DDoSAttack            
        }

    def PasswordCracker(self):
        self.game_functions.clear()
        input("Press Any Key to continue")
        if "Password Cracker" not in self.player.inventory:
            print("You do not have a password cracker, you cannot continue.")
            input()
            return
        
        print("--- Attempting Password Crack ---")
        success = 50
        if "OverClock" in self.player.inventory:
            success += 20
            self.player.inventory.remove("OverClock")
        roll = random.randint(1, 100)
        if roll > success:
            print("Password has been cracked. Here is your reward.")
            reward = random.randint(100, 200)
            self.player.update_balance(reward)
            print(f"${reward} has been added to your account.")
        else:
            self.player.detection_chance += 5
            print("Password Crack Failed. Your chance of being caught has increased.")
        if self.player.detection_chance > 50:
            self.player.inventory.remove("Password Cracker")
            print("Your password cracker has been removed from your inventory.")
        
        retry_decision = self.game_functions.TryAgain()
        if retry_decision == "PlayAgain":
            self.PasswordCracker()
        else:
            return


class GameFunctions():
    def __init__(self, player):
        self.player = player
        
    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
            
    def detection_chance(self):
        roll = random.randint(1, 100)
        if roll <= self.detection_chance:
            print("You have been detected and booted from the system!"
                  )
            consequence = random.randint(100, 200)
            self.update_balance(-consequence)
            if self.balance <= 0:
                print("You are out of money!")
            else:
                print(f"{consequence} has been removed from your account due to being caught. Your new balance is: ${self.balance}")
        else:
            print("You slipped into the system undetected.")
            
    def TryAgain(self):
        if self.counter >= 3:
            print("You have reached the maximum number of attempts.")
            self.counter = 0
            return "HackingMenu"
        print(f"You have {3 - self.counter} attempts left.")
        try_again = input("Would you like to try again? (y/n): ").lower()
        if try_again == "y":
            self.counter += 1
            return "PlayAgain"
        elif try_again == "n":
            self.counter = 0
            return "HackingMenu"
        else:
            print("Invalid input. Please try again.")
            self.TryAgain()