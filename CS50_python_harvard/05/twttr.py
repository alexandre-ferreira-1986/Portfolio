def main():
    
    # Get the input
    text = input('Input: ')
    
    # Call the function to remove vogals
    mssg = shorten(text)
    
    # Print the result
    print('Output: ', mssg)
    

def shorten(text):
    
    # Define the vogals
    vogals = ['a', 'e', 'i', 'o', 'u']
    
    # Start the string without vogals
    new_str = ''
    
    for i in text:
        # If the letter is a vogal, just continue
        if i.lower() in vogals:
            continue
        
        # If it's not a vogal, add to the new_str
        else:
            new_str += i
    
            # Return this new_str without the vogals
    return new_str
    
    
    
if __name__ == "__main__":
    main()