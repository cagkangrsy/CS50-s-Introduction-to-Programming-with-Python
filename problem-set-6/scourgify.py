
import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    filename_before = sys.argv[1]
    filename_after = sys.argv[2]

    if filename_before.split(".")[1] != "csv":
        sys.exit("Not a CSV file")

    try:
        with open(f'{filename_before}', newline='') as before, open(f"{filename_after}", 'w', newline='') as after:
            csv_reader = csv.DictReader(before)
            next(csv_reader)
            rows = []
            for line in csv_reader:
                rows.append({"first": line["name"].split(",")[-1].strip(), "last": line["name"].split(",")[0].strip(), "house": line["house"]})
            fieldnames = ["first", "last", "house"]
            csv_writer = csv.DictWriter(after, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(rows)
    except FileNotFoundError:
        sys.exit(f"Could not read {filename_before}")

if __name__ == "__main__":
    main()
