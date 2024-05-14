import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if filename.split(".")[1] != "py":
        sys.exit("Not a Python file")

    try:
        with open(filename) as file:
            lines = file.readlines()
            line_count = 0
            for line in lines:
                if line.strip() and not line.strip().startswith("#"):
                    line_count += 1
            print(line_count)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
