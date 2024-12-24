from os import system, name
import random

inventory = ["Password Cracker", "Data Sniffer", "IDS Scanner"]
balance = 0 #Changing starting balance to 0 so the player has to win some before buying items.
detection_chance = 5 #Trying to add a detection feature so that there are consequences to failure
counter = 0


def checkBalance():
    global balance
    return f"Your current balance is ${balance}"

def UpdateBalance(amount):#created update balance function so that store will correctly change balance amounts
    global balance
    balance += amount
    return balance


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def tryagain(): #turned tryagain into a function to clean up the amount of lines we had in the other functions
    global counter
    counter = 0
    if counter >= 3:
        print("You have reached the maximum number of attempts.")
        return "HackingMenu"
    print(f"You have {3 - counter} tries left.") #added to show user how many tries they have left
    try_again = input("Want to try again?:") #Added if statement to all hacking option to give the user the ability to try again.
    if try_again.lower() == "yes" or "y":
        counter += 1
        return "PlayAgain"
    else:
        counter = 0
        return "HackingMenu"

def PlayerInventory():
    clear()
    global balance
    print(f'''
                           --- Inventory ---
                        Your current balance is ${balance}
        ''')
    num = 0    
    if inventory:
        for item in inventory:
            num = num + 1  #Added numeric listing of items for user // Could change to QTY in the future!!! 
            print(f" {num}.{item}")
        print("\n")
        input("Press Any Key")
        clear()
    else:
        print("Your inventory is empty")
        input() #Pauses program to let user see their inventory
        clear()  #Clears Screen before going back to the main menu
        
def DetectionChance(): #created a detection chance function that removes money if you are caught
    global balance  # Add global VAR so the balance could be read from this function
    roll = random.randint(1, 100)
    if roll <= detection_chance:
        print("You have been detected and booted from the system.")
        consequence = random.randint(100, 200)
        balance -= consequence
        if balance < 0:
            print("You are out of money!")
        else:
            print(f"{consequence} has been removed from your account due to be caught. Your new balance is {balance}")
    else:
        print("You slipped into the system undetected.")
    
        
def PasswordCracker():
    global balance #had to add global to let the function know to pull from balance at the top
    global detection_chance #Same here with detection chance
    clear()
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
        print(f"{balance} has been added to your account.")
        print(f"Your new balance is: {balance}")
    else:
        detection_chance += 5 #add a 10% chance to being detected.
        print("Password Crack failed. Your chance of being caught has increased.")
        
    retry_decision = tryagain()
    if retry_decision == "PlayAgain":
        PasswordCracker()
    else:
        return
    
def DataExtraction():
    global balance #had to add global to let the function know to pull from balance at the top
    clear()
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
        detection_chance += 5 #add a 10% chance to being detected.
        print("Data Extraction Failed. Your chance of being caught has increased")
        
    retry_decision = tryagain() #This is used to call the try again function to ensure that counter does its job
    if retry_decision == "PlayAgain":
        DataExtraction()
    else:
        return
    
def DDoSAttack():
    global balance #had to add global to let the function know to pull from balance at the top
    clear()
    DetectionChance()
    print("--- Attempting DDoS Atttack ---")
    ip = input("Enter the target IP:")
    if ip == "127.0.0.1":
        print("Why are you hacking your home?!")
        input()
        return "HackingMenu"
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
        detection_chance += 5 #add a 10% chance to being detected.
        print("DDoS Attack Failed. Your chance of being caught has increased.")
        
    retry_decision = tryagain()
    if retry_decision == "PlayAgain":
        DDoSAttack()
    else:
        return
