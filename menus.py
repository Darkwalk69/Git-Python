# install art   pip install art
# Reference link: https://pypi.org/project/art/#description
import art
from art import *

# The only reason we are using the art module is for the tprint function


print('''
          #####################################
          #("--- Welcome Fellow Hacker! ---") #
          #  1. Hacking Options               #
          #  2. Hacking Store                 #
          #  3. View Inventory                #
          #  4. Exit                          #
          #####################################
      ''')
print('''
          #####################################
          #    --- Hackerz Paradise ---       #
          #   1. Password Cracker")           #
          #   2. Data Extraction")            #
          #   3. DDoS Attack")                #
          #   4. Main Menu")                  #
          #####################################
      ''')
print('''
          ##############################
          #   --- Inventory ---        #
          # Your Balance is ""         #
          # Items                      #
          ##############################
      ''')

tprint(" Stellar Solutions")
user_name = input("Enter Your Username: ")
password = input("Enter Your Password: ")
print(f"{user_name},{password} accepted!")

tprint(" Global Bank")
user_name = input("Enter Your Username: ")
password = input("Enter Your Password: ")
print(f"{user_name},{password} accepted!")

tprint(" Quick Loans Corporation")
user_name = input("Enter Your Username: ")
password = input("Enter Your Password: ")
print(f"{user_name},{password} accepted!")


###############################################
