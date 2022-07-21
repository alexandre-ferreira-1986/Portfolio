
def main():
    # Ask the user
    greeting = input("Greeting: ")
    
    # Print the result
    print(value(greeting))


def value(greeting):
    
    # First case - hello
    if "hello" in greeting.lower().strip():
        return '$0'
    
    # If start with 'h'
    elif greeting[0].lower() == 'h':
        return '$20'
    
    # Any other
    else:
        return '$100'
    
    
    

if __name__ == "__main__":
    main()