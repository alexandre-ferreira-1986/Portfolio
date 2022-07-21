# Import Figlet
from pyfiglet import Figlet
# Import sys to get the args
import sys
# Import random
import random

# Get the correct arguments calling the program
if len(sys.argv) == 1:
    randomFont = True
    
elif (len(sys.argv) == 3) and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    randomFont = False
else:
    print('Invalid usage')
    sys.exit(1)

# Calling Figlet
figlet = Figlet()

msg = input('Input: ')


# Printing the message
if randomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print('Invalid usage')
        sys.exit(1)
# If it's random
else:
    rand_font = random.choice(figlet.getFonts())
    figlet.setFont(font=rand_font)

    
print('Output: ')
print(figlet.renderText(msg))    