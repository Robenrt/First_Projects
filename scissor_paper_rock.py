import random

def game():
    while True:
        ask = input("Scissor, Paper, Rock? (s/p/r): ").strip().lower()
        options = ("s", "p", "r")
        computer = random.choice(options)

        if ask not in options:
            print("Invalid Choice! Please try again: ")
        else:
            if (computer=="s" and ask == "p") or (computer=="r" and ask=="p") or (computer=="r" and ask=="s"):
                print("Computer won!")
            elif (ask=="r" and computer=="s") or (ask=="s" and computer=="p") or (ask=="r" and computer=="p"):
                print("You won!")
            elif computer==ask:
                print("Draw!")
        ask= input("Do you want to continue again? ").strip().lower()
        if "y" in ask:
            continue
        else:
            break


game()