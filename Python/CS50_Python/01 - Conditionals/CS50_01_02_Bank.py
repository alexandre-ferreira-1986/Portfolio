
# Ask the user
greeting = input("Greeting: ")

# Conditionals
if "hello" in greeting.lower().strip():
    print('$0')
elif greeting[0].lower() == 'h':
    print('$20')
else:
    print('$100')