import DEV_HackingGameFunctions
import DEV_HackingGame
# After logging in, keep this menu at the top of the screen for menu choice
# Add logout option, screen destroyed
# Idea to keep this portion of the game simple as possible.
print('''
          #################################
          #  Welcome to Stellar Solutions #
          #################################
      ''')

    #Hacking Menu :  Tool's that are available


print('''
          #######################################
          #  Welcome to Quick Loans Corporation #
          #######################################
      ''')
    # Hacking Menu :  Tool's that are available


print('''
          ###########################
          #  Welcome to Global Bank #
          ###########################
      ''')
    # Hacking Menu :  Tool's that are available






# Hacks

print("Scanning Wifi Networks...")
    success = random.randint(1, 100)
    if success > 20:
        print("Accessible Wifi Network Found")
    elif success <= 10:
        detection_chance += 5
        print("You were detected. IP address has been logged and banned.")
    else:
        print("Failed to locate network.")
        return MainMenu()

    print("Scrubbing Hard Drive for Project Galaxy Files...")
    success = random.randint(1, 100)
    if success > 30:
        print("Project Galaxy Files Found. Password Required.")
    elif success <= 10:
        detection_chance += 10
        print("You were detected. IP address has been logged and banned.")
    else:
        print("Failed to locate Project Galaxy Files.")
        return MainMenu()

    print("Cracking Password...")
    success = random.randing(1, 100)
    if success > 40:
        print("Password Cracked. Files Downloaded. Preparing Virus Injection for escape.")
    elif success <= 10:
        detection_chance += 15
        print("You were detected. IP address has been logged and banned.")
    else:
        print("Password Cracking Failed.")
        return MainMenu()

    print("Injecting Virus into Mainframe...")
    success = random.randint(1, 100)
    if success > 50:
        print("Virus Injected. Files Downloaded. Contract Complete.")
        balance += 1000
        print("You have been paid $1000.")
    elif success <= 10:
        detection_chance += 20
        print("You were detected. IP address has been logged and banned.")
    else:
        print("Virus Injection Failed.")
        return MainMenu()