from operator import inv
import random

inventory = []

def MainMenu():
    choice = ""
    while choice != 4:  
        print("--- Welcome Fellow Hacker! ---")
        print("1. Hacking Options")
        print("2. Hacking Store")
        print("3. View Inventory")
        print("4. Exit")
        choice = int(input("Enter your selection:\n"))
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
    
def HackingMenu():
    print("--- Here are your available hacks ---")
    print("1. Password Cracker")
    print("2. Data Extraction")
    print("3. DDoS Attack")
    print("4. Main Menu")
    choice = int(input("Please make a selection:\n"))
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
        return HackingMenu()
    
def HackingStore():
    print("--- Welcome to the Hacking Emporium ---")
    print("1. Password Cracker Boost. $100")
    print("2. Data Sniffer. $200")
    print("3. Servers to assist with DDoS Attack. $300")
    print("4. Main Menu")
    choice = int(input("Please make a selection:\n"))
    if choice == 1:
        print("Adding Password Cracker to inventory")
        inventory.append("Password Cracker")
    elif choice == 2:
        print("Adding Data Sniffer to Inventory")
        inventory.append("Data Sniffer")
    elif choice == 3:
        print("Adding Servers to Inventory")
        inventory.append("Servers")
    elif choice == 4:
        MainMenu()
    else:
        print("Invalid selection. Please choose a correct option")
        HackingStore()
        
    continue_shopping = input("would you like to keep shopping (yes/no):\n")
    if continue_shopping.lower() == "yes":
        HackingStore()
    else:
        MainMenu()
    
def PlayerInventory():
    print("--- Here is your Inventory ---")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty")
        
def PasswordCracker():
    print("---  Attempting Password Crack ---")
    success = 50
    if "Password Cracker" in inventory:
        success += 20
    roll = random.randint(1, 100)
    if roll > success:
        print("Password has been cracked")
    else:
        print("Password Crack failed")
    HackingMenu()
    
def DataExtraction():
    print("--- Attempting Data Extraction ---")
    success = 40
    if "Data Sniffer" in inventory:
        success += 20
    roll = random.randint(1, 100)
    if roll > success:
        print("Data Extraction Successful")
    else:
        print("Data Extraction Failed")
    HackingMenu()
    
def DDoSAttack():
    print("--- Attempting DDoS Atttack ---")
    success = 20
    if "Servers" in inventory:
        success += 20
    roll = random.randint(1, 100)
    if roll > success:
        print("DDoS Attack Successful")
    else:
        print("DDoS Attack Failed")
    HackingMenu()   
    
if __name__ == "__main__":
    MainMenu()