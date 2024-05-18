import sys
import PIL
from PIL import Image

def main():
    file_input = sys.argv[1]
    file_output = sys.argv[2]
    extension_list = ["png", "jpg", "jpeg"]

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if file_input.split(".")[-1] not in extension_list:
        sys.exit("Invalid input")
    if file_output.split(".")[-1] not in extension_list:
        sys.exit("Invalid output")
    if file_input.split(".")[-1] != file_output.split(".")[-1]:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(file_input) as input, Image.open("shirt.png") as shirt:
            input = PIL.ImageOps.fit(image = input, size = shirt.size)
            input.paste(shirt, shirt)
            input.save(file_output)
    except FileNotFoundError:
        sys.exit(f"Could not read {file_input}")

if __name__ == "__main__":
    main()
