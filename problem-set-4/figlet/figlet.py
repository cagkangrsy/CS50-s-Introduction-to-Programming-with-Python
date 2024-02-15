from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    input_text = input("Input: ")
    font = random.choice(seq)
    figlet.setFont(font=font)
    print(figlet.renderText(input_text))
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    else:
        if sys.argv[2] not in font_list:
            sys.exit("Invalid usage")
        else:
            input_text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(input_text))
else:
    sys.exit("Invalid usage")
