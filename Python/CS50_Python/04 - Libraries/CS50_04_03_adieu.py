import inflect

p = inflect.engine()

# List with the names
names = []

# Loop to get the names
while True:
    try:
        name = input('Name: ')
        names.append(name)
    
    # Stop when press Ctr+D
    except EOFError:
        
        break

# Print the message    
print(f'Adieu, adieu, to {p.join(names)}')