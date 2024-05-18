import re


def main():
    print(count(input("Text: ")))


def count(s):
    um_count = 0
    s_no_punct = re.sub(r'\W+', ' ', s)
    words = s_no_punct.split(" ")
    print(words)
    for word in words:
        if word in ["um", "UM", "Um"]:
            um_count += 1
    return um_count

...


if __name__ == "__main__":
    main()
