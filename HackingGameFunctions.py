from os import system, name
import random

inventory = ["Password Cracker"]
balance = 0 #Changing starting balance to 0 so the player has to win some before buying items.
detection_chance = 5 #Trying to add a detection feature so that there are consequences to failure
counter = 0




def checkBalance():
    global balance
    return f"Your current balance is ${balance}"


# created update balance function so that store will correctly change balance amounts
def UpdateBalance(amount):
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


def tryagain():  # turned tryagain into a function to clean up the amount of lines we had in the other functions
    global counter
    if counter >= 3:
        print("You have reached the maximum number of attempts.")
        counter = 0
        return "HackingMenu"
    print(f"You have {3 - counter} tries left.") #added to show user how many tries they have left
    try_again = input("Want to try again?:").lower() # Added lower to the users input before it hits the logic
    if try_again == "yes" or try_again == "y": #Corrected OR statement

        counter += 1
        return "PlayAgain"
    elif try_again == "no" or try_again == "n": #Corrected OR statement
        counter = 0
        return "HackingMenu"
    else:
        print("Please input a valid option") # Added additional error control
        return tryagain()

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
            num = num + 1  # Added numeric listing of items for user // Could change to QTY in the future!!!
            print(f" {num}.{item}")
        print("\n")
        input("Press Any Key")
        clear()
    else:
        print("Your inventory is empty")
        input()  # Pauses program to let user see their inventory
        clear()  # Clears Screen before going back to the main menu


def DetectionChance():  # created a detection chance function that removes money if you are caught
    global balance  # Add global VAR so the balance could be read from this function
    roll = random.randint(1, 100)
    if roll <= detection_chance:
        print("You have been detected and booted from the system.")
        consequence = random.randint(100, 200)
        balance -= consequence
        if balance <= 0:
            print("You are out of money!")
        else:
            print(
                f"{consequence} has been removed from your account due to be caught. Your new balance is {balance}")
    else:
        print("You slipped into the system undetected.")


def PasswordCracker():
    global balance  # had to add global to let the function know to pull from balance at the top
    global detection_chance  # Same here with detection chance
    clear()
    DetectionChance()
    input("Press any key to continue") #Added input to let use see out put before rest of text appears on screen.
    if "Password Cracker" not in inventory:
            print("You do not have a password cracker, you cannot continue")
            input()
            return

    print("---  Attempting Password Crack ---")
    success = 50
    if "OverClock" in inventory:
        success += 20
        inventory.remove("OverClock")        
    roll = random.randint(1, 100)
    if roll > success:
        print("Password has been cracked. Here is your reward.")
        # Changed it to randomly add value to balance
        balance += random.randint(100, 200)
        print(f"{balance} has been added to your account.")
    else: 
        detection_chance += 5 #add a 10% chance to being detected.
        print("Password Crack failed. Your chance of being caught has increased.")
    if detection_chance > 50:
        inventory.remove("Password Cracker")
        print("Password Cracker has deleted from your system")
        
    retry_decision = tryagain()
    if retry_decision == "PlayAgain":
        PasswordCracker()
    else:
        return


def DataExtraction():
    global balance  # had to add global to let the function know to pull from balance at the top
    clear()
    DetectionChance()
    print("--- Attempting Data Extraction ---")
    success = 40
    if "Data Sniffer" in inventory:  # Need to figure out how to use the item and remove it from inventory
        success += 20
        inventory.remove("Data Sniffer")
        print(f"Here is your remaining inventory: {inventory}")
    roll = random.randint(1, 100)
    if roll > success:
        print("Data Extraction Successful. Here is your reward.")
        # Changed it to randomly add value to balance
        balance += random.randint(200, 300)
        print(f"Your new balance is: {balance}")
    else:
        global detection_chance  # Same here with detection chance
        detection_chance += 5  # add a 10% chance to being detected.
        print("Data Extraction Failed. Your chance of being caught has increased")

    # This is used to call the try again function to ensure that counter does its job
    retry_decision = tryagain()
    if retry_decision == "PlayAgain":
        DataExtraction()
    else:
        return


def DDoSAttack():
    global balance  # had to add global to let the function know to pull from balance at the top
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
    if "Servers" in inventory:  # Need to figure out how to use the item and remove it from inventory
        success += 20
        inventory.remove("Servers")
        print(f"Here is your remaining inventory: {inventory}")
    roll = random.randint(1, 100)
    if roll > success:
        print("DDoS Attack Successful. Here is your reward.")
        # Changed it to randomly add value to balance
        balance += random.randint(300, 400)
        print(f"Your new balance is: {balance}")
    else:
        global detection_chance  # Same here with detection chance
        detection_chance += 5  # add a 10% chance to being detected.
        print("DDoS Attack Failed. Your chance of being caught has increased.")

    retry_decision = tryagain()
    if retry_decision == "PlayAgain":
        DDoSAttack()
    else:
        return
