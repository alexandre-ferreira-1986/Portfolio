def main():
    
    # Ask the input
    fuel = input('Fraction: ')
    
    frac = convert(fuel)
    
    result = gauge(frac)
    
    print(result)

def convert(fuel):
    # Starting the Loop
    while True:
        

        
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
                val = int(frac*100)
                return val
            else:
                fuel = input('Fraction: ')
                pass
        
        except (ValueError, ZeroDivisionError):
            raise

def gauge(frac):
            
    if frac <= 1:
        return 'E'
    elif frac >= 99:
        return 'F'
    else:
        return f'{frac}%'
    
    
    
if __name__ == "__main__":
    main()