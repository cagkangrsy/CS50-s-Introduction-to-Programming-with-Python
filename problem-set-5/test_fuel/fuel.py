def main():
    while True:
        try:
            fraction_input = input("Enter fraction as X/Y: ")
            print(gauge(convert(fraction_input)))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction_input):
    if '/' not in fraction_input:
        raise ValueError
    nominator, denominator = fraction_input.split('/')
    if '.' in nominator or '.' in denominator:
        raise ValueError
    X = int(nominator)
    Y = int(denominator)
    if Y == 0:
        raise ZeroDivisionError
    if X > Y:
        raise ValueError
    percentage = round(X / Y * 100)
    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
