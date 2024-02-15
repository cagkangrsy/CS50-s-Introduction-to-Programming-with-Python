import random

def main():
    points = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        print(f"{x} + {y} =")
        correct = False
        for i in range(3):
            sum = int(input())
            if sum == x + y:
                points += 1
                correct = True
                break
            else:
                print("EEE")
        if not correct:
            print(x + y)
    print(points)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, (10**level - 1))
    else:
        return random.randint(10 ** (level - 1), ((10**level) - 1))

if __name__ == "__main__":
    main()
