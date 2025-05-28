import random

def matching_num():
    number = random.randint(1,100)
    while True:
        try:
            frage = int(input("Guess the number between 1 and 100: "))
            if frage > number:
                print("Too High!")
            elif frage < number:
                print("Too Low")
            else:
                print("Right Guess!")
                break
        except ValueError:
            print("Please enter a valid number.")

matching_num()