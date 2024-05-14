import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if filename.split(".")[1] != "csv":
        sys.exit("Not a CSV file")

    try:
        with open(filename) as file:
            lines = file.readlines()
            rows = []
            for line in lines:
                rows.append(line.strip().split(","))
            print(rows)
            print(tabulate(rows, headers="firstrow",tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
