#make comments!!!
from operator import inv
import os
import random

inventory = []
balance = 0 #Changing starting balance to 0 so the player has to win some before buying items.
detection_chance = 10 #Trying to add a detection feature so that there are consequences to failure

def MainMenu():
    os.system("cls")
    choice = ""
    while choice != 4:  
        print("--- Welcome Fellow Hacker! ---")
        print("1. Hacking Options")
        print("2. Hacking Store")
        print("3. View Inventory")
        print("4. Exit")
        try:
            choice = int(input("Enter your selection:\n"))
        except ValueError:
            print("Invalid Input! Please enter a number.")
        if choice == 1:
            print("Now displaying all available hacking options")
            HackingMenu()
        elif choice == 2:
            print("Now displaying the Hacking Store")
            HackingStore()
        elif choice == 3:
            print("Now displaying your current stats")
            PlayerInventory()
        elif choice == 4:
            print("Exiting game. Goodbye!")
            exit()
        else:
            print("Invalid selection. Please choose a correct option")
            MainMenu()

    
def HackingMenu(): #Consider letting the user attempt the hack attempt more than 1 time before forcing to the hacking menu 2 times? IDS system will be activated!!! 
    os.system("cls")
    print("--- Here are your available hacks ---")
    print("1. Password Cracker")
    print("2. Data Extraction")
    print("3. DDoS Attack")
    print("4. Main Menu")
    try:
        choice = int(input("Please make a selection:\n"))
    except ValueError:
        print("Invalid Input!. Please enter a number.")
    if choice == 1:
        print("Preparing Password Cracking Software")
        PasswordCracker()
    elif choice == 2:
        print("Preparing Data Extraction Software")
        DataExtraction()
    elif choice == 3:
        print("Preparing DDoS Attack")
        DDoSAttack()
    elif choice == 4:
        MainMenu()
    else:
        print("Invalid selection. Please choose a correct option")
        HackingMenu()
    
def HackingStore():
    os.system("cls")
    print("--- Welcome to the Hacking Emporium ---")
    print(f"Your current balance is: ${balance}") #Showing player what their balance is everytime they open the store up to help them keep track of their money.
    print("1. Password Cracker Boost. $100")
    print("2. Data Sniffer. $200")
    print("3. Servers to assist with DDoS Attack. $300")
    print("4. Main Menu")
    try:
        choice = int(input("Please make a selection:\n"))
    except ValueError:
        print("Invalid input! Please enter a number.")
    if choice == 1:
        print("Adding Password Cracker to inventory")
        inventory.append("Password Cracker")
        balance -= 100
    elif choice == 2:
        print("Adding Data Sniffer to Inventory")
        inventory.append("Data Sniffer")
        balance -= 200
    elif choice == 3:
        print("Adding Servers to Inventory")
        inventory.append("Servers")
        balance -= 300
    elif choice == 4:
        MainMenu()
    else:
        print("Invalid selection. Please choose a correct option")
        return HackingStore()
    
    next_action = input("Would you like to continue shopping? (yes/no): ")
    if next_action.lower() == "yes":
        HackingStore()
    else:
        MainMenu()
    
def PlayerInventory():
    num = 0
    os.system("cls")
    print("--- Here is your Inventory ---")
    if inventory:
        for item in inventory:
            num = num + 1  #Added numeric listing of items for user // Could change to QTY in the future!!! 
            print(f"{num}.{item}")
    else:
        print("Your inventory is empty")
        input() #Pauses program to let user see their inventory
        os.system("cls")  #Clears Screen before going back to the main menu
        
def DetectionChance(): #created a detection chance function that removes money if you are caught
    roll = random.randint(1, 100)
    if roll <= detection_chance:
        print("You have been detected and booted from the system.")
        consequence = random.randint(100, 200)
        balance -= consequence
        print(f"{consequence} has been removed from your account due to be caught. Your new balance is {balance}")
    else:
        print("You slipped into the system undetected.")
    
        
def PasswordCracker():
    global balance #had to add global to let the function know to pull from balance at the top
    os.system("cls")
    DetectionChance()
    print("---  Attempting Password Crack ---")
    success = 50
    if "Password Cracker" in inventory:
        success += 20
        inventory.remove("Password Cracker")
        print(f"Here is your remaining inventory: {inventory}")
    roll = random.randint(1, 100)
    if roll > success:
        print("Password has been cracked. Here is your reward.")
        balance += random.randint(100,200) #Changed it to randomly add value to balance
        print(f"Your new balance is: {balance}")
    else:
        global detection_chance #Same here with detection chance
        detection_chance += 10 #add a 10% chance to being detected.
        print("Password Crack failed. Your chance of being caught has increased.")
        
    try_again = input("Want to try again?:") #Added if statement to all hacking option to give the user the ability to try again.
    if try_again.lower() == "yes":
        PasswordCracker()
    else:
        HackingMenu()
    
def DataExtraction():
    global balance #had to add global to let the function know to pull from balance at the top
    os.system("cls")
    DetectionChance()
    print("--- Attempting Data Extraction ---")
    success = 40
    if "Data Sniffer" in inventory: #Need to figure out how to use the item and remove it from inventory
        success += 20
        inventory.remove("Data Sniffer")
        print(f"Here is your remaining inventory: {inventory}")
    roll = random.randint(1, 100)
    if roll > success:
        print("Data Extraction Successful. Here is your reward.")
        balance += random.randint(200, 300) #Changed it to randomly add value to balance
        print(f"Your new balance is: {balance}")
    else:
        global detection_chance #Same here with detection chance
        detection_chance += 10 #add a 10% chance to being detected.
        print("Data Extraction Failed. Your chance of being caught has increased")
        
    try_again = input("Want to try again?:")
    if try_again.lower() == "yes":
        DataExtraction()
    else:
        HackingMenu()
    
def DDoSAttack():
    global balance #had to add global to let the function know to pull from balance at the top
    os.system("cls")
    DetectionChance()
    print("--- Attempting DDoS Atttack ---")
    ip = input("Enter the target IP:")
    if ip == "127.0.0.1":
        print("Why are you hacking your home?!")
        input()
        HackingMenu()
    else:
        print(f"--- Attempting DDoS Atttack --- on {ip}")
    success = 20
    if "Servers" in inventory: #Need to figure out how to use the item and remove it from inventory
        success += 20
        inventory.remove("Servers")
        print(f"Here is your remaining inventory: {inventory}")
    roll = random.randint(1, 100)
    if roll > success:
        print("DDoS Attack Successful. Here is your reward.")
        balance += random.randint(300, 400) #Changed it to randomly add value to balance
        print(f"Your new balance is: {balance}")
    else:
        global detection_chance #Same here with detection chance
        detection_chance += 10 #add a 10% chance to being detected.
        print("DDoS Attack Failed. Your chance of being caught has increased.")
        
    try_again = input("Want to try again?: ")
    if try_again.lower() == "yes":
        DDoSAttack()
    else:
        HackingMenu()
    
if __name__ == "__main__":
    MainMenu()