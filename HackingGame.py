#make comments!!!
from HackingGameFunctions import DetectionChance, PasswordCracker, DataExtraction, DDoSAttack, PlayerInventory, clear, checkBalance

def MainMenu():
    clear()
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
    clear()
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
        result = PasswordCracker()
        if result == "PlayAgain": #Added if statements to all choice to coincide with the fixed try again choices in hackinggamefunctions
            PasswordCracker()
        else:
            HackingMenu()
    elif choice == 2:
        result = DataExtraction()
        if result == "PlayAgain":
            DataExtraction()
        else:
            HackingMenu()
    elif choice == 3:
        result = DDoSAttack()
        if result == "PlayAgain":
            DDoSAttack()
        else:
            HackingMenu()
    elif choice == 4:
        MainMenu()
    else:
        print("Invalid selection. Please choose a correct option")
        HackingMenu()
    
def HackingStore():
    global balance
    clear()
    print("--- Welcome to the Hacking Emporium ---")
    message = checkBalance(None)  # Added Balance for player to see their money while shopping
    print(message)

    print("1. Password Cracker Boost. $100")
    print("2. Data Sniffer. $200")
    print("3. Servers to assist with DDoS Attack. $300")
    print("4. Main Menu")
    try:
        choice = int(input("Please make a selection:\n"))
    except ValueError:
        print("Invalid input! Please enter a number.")
    if choice == 1:
        if balance < 100:
            print("You don't have enough money!")
        else:
            print("Adding Password Cracker to inventory")
            inventory.append("Password Cracker")
            balance -= 100
    elif choice == 2:
        if balance < 200:
            print("You don't have enough money!")
        else:
            print("Adding Data Sniffer to Inventory")
            inventory.append("Data Sniffer")
            balance -= 200
    elif choice == 3:
        if balance < 300:
            print("You don't have enough money!")
        else:
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

if __name__ == "__main__":
    MainMenu()