def convert(input_string):
    converted_string = input_string.replace(':)', '🙂').replace(':(', '🙁')
    return converted_string

def main():
    input_string = input()
    print(convert(input_string))

main()
