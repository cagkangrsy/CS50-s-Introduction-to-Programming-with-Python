# mplement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file.

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python lines.py filename")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename
        ) as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if line.strip() and not line.strip().startswith("#"):
                    count += 1
            print(count)
    except FileNotFoundError:
        print(f"Cannot find file: {filename}")
        sys.exit(1)