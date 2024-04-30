def main():
    input_text = input("Input: ")
    print("Output:", shorten(input_text))

def shorten(word):
    shortened_word = ''

    for letter in word:
        if letter in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
            continue
        else:
            shortened_word += letter
    return shortened_word

if __name__ == "__main__":
    main()
