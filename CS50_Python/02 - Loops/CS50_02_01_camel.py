# User input
camel = input('camelCase: ')

# empty list
word = []

# Loop
for i in camel:
    #Check if is upper
    if i.isupper():
        word.append("_" + i.lower())
    else:
        word.append(i)

# Convert a list to String        
converted = ''.join([str(item) for item in word])

print(converted)