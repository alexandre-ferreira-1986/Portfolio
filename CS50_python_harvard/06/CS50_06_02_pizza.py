import sys
import csv
from tabulate import tabulate


def main():
    
    # Check the input
    check_command()
    
    # Create the table
    table = []
    
    # Open the file CSV
    try:
        
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
        
    except FileNotFoundError:
        sys.exit('File does not exist')
    
    # Tabulate: https://pypi.org/project/tabulate/
    tabul = tabulate(table, headers = 'firstrow', tablefmt="grid")
    
    print(tabul)


def check_command():    
    
    # len of the arguments
    len_argv = len(sys.argv)
    
    # If the user don't pass anything
    if len_argv < 2:
        sys.exit('Too few command-line arguments')
    
    # If the user pass more than 1 argument
    if len_argv > 2:
        sys.exit('Too many command-line arguments')
    
    # If the user input an file that is not ".csv""
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')



if __name__ == '__main__':
    main()