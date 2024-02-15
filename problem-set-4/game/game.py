import random

while True:
    try:
        level = int(input("Level: "))
        number = random.randint(1, level)

        while True:
            guess = int(input("Guess: "))
            if guess < number:
                print("Too small!")
                continue
            if guess > number:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break
        break
    except ValueError:
        continue
