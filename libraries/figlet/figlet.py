import sys
from pyfiglet import Figlet
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 1:
        name = input("Input: ")
        print(figlet.renderText(name))
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            f = sys.argv[2]
            if f in fonts:
                name = input("Input: ")
                figlet.setFont(font = f)
                print(figlet.renderText(name))
            else: 
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")