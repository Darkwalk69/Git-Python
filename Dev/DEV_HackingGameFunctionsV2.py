from os import system, name
from art import tprint
import random

class Player:
    def __init__(self):
        self.inventory = []
        self.balance = 0
        self.detection_chance = 5
        
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
            