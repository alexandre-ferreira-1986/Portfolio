import sys
import csv

def main():
    
    check_command()
    
    # Create the table
    output = []
    
    # Open the file CSV
    try:
        
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                split_name = row['name'].split(',')
                output.append({'first': split_name[1].lstrip(), 'last': split_name[0], \
                               'house': row['house']})                   
        
    except FileNotFoundError:
        sys.exit('File does not exist')


        
    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        
        writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
        
        for row in output:
            writer.writerow({'first': row['first'], 'last': row['last'], \
                             'house': row['house']})
    
    

def check_command():    
    
    # len of the arguments
    len_argv = len(sys.argv)
    
    # If the user don't pass anything
    if len_argv < 3:
        sys.exit('Too few command-line arguments')
    
    # If the user pass more than 1 argument
    if len_argv > 3:
        sys.exit('Too many command-line arguments')
    
    # If the user input an file that is not ".csv""
    for i in range(1, 2):
        if '.csv' not in sys.argv[i]:
            sys.exit('Not a CSV file')
        

if __name__ == '__main__':
    main()