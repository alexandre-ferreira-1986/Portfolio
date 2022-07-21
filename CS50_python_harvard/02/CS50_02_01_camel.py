camel = input('camelCase: ')

word = []
for i in camel:
    #Check if is upper
    if i.isupper():
        word.append("_" + i.lower())
    else:
        word.append(i)

# Convert a list to String        
converted = ''.join([str(item) for item in word])

print(converted)