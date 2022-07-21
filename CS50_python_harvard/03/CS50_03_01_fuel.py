# Starting the Loop
while True:
    
    # Ask the input
    fuel = input('Fraction: ')
    
    try:
        # Split the input
        num, den = fuel.split('/')
        
        # Converting to integers
        num_int = int(num)
        den_int = int(den)
        
        # Calculate
        frac = num_int/den_int
        
        # Checking the conditions of the problem
        if frac <= 1:
            break
    
    except (ValueError, ZeroDivisionError):
        raise

# Transform frac to percentage (mult by 100)
perc = frac * 100

if perc <= 1:
    print('E')
elif perc >= 99:
    print('F')
else:
    print(f'{perc}%')

