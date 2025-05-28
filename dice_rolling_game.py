# Ask: roll the dice?
# Loop
# If user enters y
#     Generate two random numbers
#      Print them
# If user enters n 
#     print thank you message
#     Terminate
# else
# print Invalid choice

import random



def rolling_dice():
    while True:
        match input("Do you want to roll a dice? ").strip().upper():
            case "Y":
                result1=  random.randint(1,6)
                result2=  random.randint(1,6)
                print(f"{result1}, {result2}")
                
            case "N":
                print("Thank you!")
                break
            case _:
                print("Invalid Choice! Please try again.")
                break


rolling_dice()