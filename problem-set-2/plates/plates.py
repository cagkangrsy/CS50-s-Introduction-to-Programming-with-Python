def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    def start_with_2_letter(s):
        while len(s) > 1:
            if s[0].isdigit() or s[1].isdigit():
                return False
            else:
                return True
        return False

    def plate_length(s):
        if len(s) >= 2 and len(s) <= 6:
            return True
        else:
            return False

    def number_check(s):
        if s.isalpha():
            return True
        else:
            for index, letter in enumerate(s):
                if letter.isdigit():
                    if s[0:index].isalpha():
                        if letter == '0':
                            return False
                        else:
                            if s[index:-1].isdigit():
                                return True
                            else:
                                return False

    if (start_with_2_letter(s) and plate_length(s) and number_check(s)):
        return True
    else:
        return False

main()
