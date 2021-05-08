# use "def" to mark the start of a func header
# use : to mark the end of a func header
# optional documentation string (docstring) to descrbe what the func does

# import random for random operations
import random

def D20(rolls):
    """This function will roll D20s and print the outcome."""
    print("You rolled a D20 and got:")
    print(random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # prints random # from list of #'s

def D12(rolls):
    """This function will roll D12s and print the outcome."""
    print("You rolled a D12 and got:")
    print(random.randrange(0, 12))

def user_input(dice,rolls):
    """ This function is a switch statement as a menu to choose while dice you want to roll """
    switcher = {
        0: D20(rolls), 
        1: D12(rolls),
    }
    return switcher.get(dice, "Invalid dice choice.") # must include a return for switcher to work 

dice = 0 # you dont need to put the type when declaring!
print("0 - D20\n1 - D12\n2 - D10\n3 - D8\n4 - D6\n5 - D4")
dice = input("Please choose from the list above which dice you would like to roll:\n")
rolls = input("How many times would you like to roll?\n")
print("\nRolling dice...\n")
user_input(dice,rolls)