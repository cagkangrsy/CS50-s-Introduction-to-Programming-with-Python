while True:
    try:
        fraction_input = input("Enter fraction as X/Y: ")
        if '/' not in fraction_input:
            continue
        fraction = fraction_input.split('/')
        nominator = fraction[0]
        denominator = fraction[1]
        X = int(nominator)
        Y = int(denominator)
        if ('.' in nominator) or ('.' in denominator) or (X > Y):
            continue
        percentage = round(X / Y * 100)
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
