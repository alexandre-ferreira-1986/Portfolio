import sys

def main():
    
    # Check if the user input the corret argument
    check_command()
    
    # Open the file
    try:
        file = open(sys.argv[1], 'r')
        lines = file.readlines()
        
        #print(lines)
        
    except FileNotFoundError:
        sys.exit('File does not exist')
    
    # Check each line
    counter = 0
    for line in lines:
        if check_false_lines(line) == False:
            counter += 1
    
    # Print the value of lines
    print(counter)

def check_command():    
    
    # len of the arguments
    len_argv = len(sys.argv)
    
    # If the user don't pass anything
    if len_argv < 2:
        sys.exit('Too few command-line arguments')
    
    # If the user pass more than 1 argument
    if len_argv > 2:
        sys.exit('Too many command-line arguments')
    
    # If the user input an file that is not ".py""
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a Python file')
        

def check_false_lines(line):
     if line.isspace():
         return True
     if line.lstrip().startswith('#'):
         return True
     
     return False


if __name__ == '__main__':
    main()