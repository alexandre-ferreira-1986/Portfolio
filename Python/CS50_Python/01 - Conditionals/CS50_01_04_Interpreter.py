# Ask the Expression
exp = input('Expression: ')

# Isolate the variables
x, y, z = exp.split(' ')

# convert to float
x, z = float(x), float(z)

# Create a result
if y == '+':
    result = float(x + z)
elif y == '-':
    result = float(x - z)
elif y == '*':
    result = float(x * z)
elif y == '/':
    result = float(x / z)

# Print the result
print(f'{result:.1f}')