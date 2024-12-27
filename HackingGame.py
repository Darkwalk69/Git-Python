print("Loading HackingGame")

# make comments!!!
from HackingGameFunctions import DetectionChance, HackingContracts, PasswordCracker, DataExtraction, DDoSAttack, PlayerInventory, clear, checkBalance, UpdateBalance, StellarSolutions, GlobalBank, QuickLoansCorporation

# Reminder comment. If you are trying to have code from HackingGameFunctions work with HackingGame and it is now working. Try creating a function and importing it in.


def MainMenu():  # Updated Menu to reflect adding in HackingContracts
    clear()
    choice = ""
    while choice != 6:
        print('''
          #####################################
          #  --- Welcome Fellow Hacker! ---   #
          #  1. Available Hacks               #
          #  2. Hacking Targets               #
          #  3. Hacking Contracts             #
          #  4. Hacking Store                 #
          #  5. View Inventory                #
          #  6. Exit                          #
          #####################################
        ''')
        try:
            choice = int(input("Enter your selection:\n"))
        except ValueError:
            print("Invalid Input! Please enter a number.")
        if choice == 1:
            print("Now displaying all available hacking options")
            HackingMenu()
        elif choice == 2:  # Adding HackingTargets to MainMenu
            print("Now accessing available hacking contracts.")
            HackingTargets()
        elif choice == 3:  # Added HackingContracts to MainMenu so user can get contract here then go to target menu to do contracts.
            print("Now displaying available hacking contracts.")
            HackingContracts()
        elif choice == 4:
            print("Now displaying the Hacking Store")
            HackingStore()
        elif choice == 5:
            print("Now displaying your current stats")
            PlayerInventory()
        elif choice == 6:
            print("Exiting game. Goodbye!")
            exit()
        else:
            print("Invalid selection. Please choose a correct option")
            MainMenu()


def HackingMenu():  # Consider letting the user attempt the hack attempt more than 1 time before forcing to the hacking menu 2 times? IDS system will be activated!!!
    clear()
    print('''
          #####################################
          #  --- Welcome Fellow Hacker! ---   #
          #  1. Password Cracker              #
          #  2. Data Extraction               #
          #  3. DDos Attack                   #
          #  4. Main Menu                     #
          #####################################
        ''')
    try:
        choice = int(input("Please make a selection:\n"))
    except ValueError:
        print("Invalid Input!. Please enter a number.")
    if choice == 1:
        result = PasswordCracker()
        if result == "PlayAgain":  # Added if statements to all choice to coincide with the fixed try again choices in hackinggamefunctions
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
    # Moved imports down here and removed global values fixed issue for balance and inventory alignment.
    from HackingGameFunctions import balance, inventory
    clear()
    print("--- Welcome to the Hacking Emporium ---")
    message = checkBalance()  # Added Balance for player to see their money while shopping
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
        # imported updatebalance function with amount argument. All lines in store changes and function import is at top of code.
        if UpdateBalance(0) < 100:
            print("You don't have enough money!")
        # added elif statement to stop purchases when in negative
        elif UpdateBalance(-100) < 0:
            print("You don't have enough Money!")
        else:
            print("Adding Password Cracker to inventory")
            inventory.append("Password Cracker")
            UpdateBalance(-100)
    elif choice == 2:
        if UpdateBalance(0) < 200:
            print("You don't have enough money!")
        elif UpdateBalance(-200) < 0:
            print("You don't have enough Money!")
        else:
            print("Adding Data Sniffer to Inventory")
            inventory.append("Data Sniffer")
            UpdateBalance(-200)
    elif choice == 3:
        if UpdateBalance(0) < 300:
            print("You don't have enough money!")
        elif UpdateBalance(-300) < 0:
            print("You don't have enough Money!")
        else:
            print("Adding Servers to Inventory")
            inventory.append("Servers")
            UpdateBalance(-300)
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


def HackingTargets():  # Created HackingContracts function menu to display available contracts
    clear()
    print('''
          #####################################
          #  --- Hacking Contracts ---        #
          #  1. Stellar Solutions             #
          #  2. Global Bank                   #
          #  3. Quick Loan Corporation        #
          #  4. Main Menu                     #
          #####################################''')
    try:
        choice = int(input("Please make a selection:\n"))
    except ValueError:
        print("Invalid Input! Please enter a number.")
    if choice == 1:
        StellarSolutions()
    elif choice == 2:
        GlobalBank()
    elif choice == 3:
        QuickLoansCorporation()
    elif choice == 4:
        MainMenu()
    else:
        print("Invalid Selection. Please choose a correct option")
        return HackingTargets()


if __name__ == "__main__":
    MainMenu()
