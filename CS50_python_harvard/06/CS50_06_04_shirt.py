import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    
    check_command()

    try:
        
        imagefile = Image.open(sys.argv[1])
        
    except FileNotFoundError:
        sys.exit('Input does not exist')
        
    # Open the shirt
    shirt = Image.open('shirt.png')
    
    # Resize the shirt
    size = shirt.size

    # Resize the muppet
    muppet = ImageOps.fit(imagefile, size)
    
    # Overlay the image on top of another
    muppet.paste(shirt, shirt)

    # save the photo
    muppet.save(sys.argv[2])

def check_command():    
    
    # len of the arguments
    len_argv = len(sys.argv)
    
    # If the user don't pass anything
    if len_argv < 3:
        sys.exit('Too few command-line arguments')
    
    # If the user pass more than 1 argument
    if len_argv > 3:
        sys.exit('Too many command-line arguments')
    
    # Check files
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    
    
    if check_extension(file1[1]) == False:
        sys.exit('Invalid input')
    if  check_extension(file2[1]) == False:
        sys.exit('Invalid output')
        
    if file1[1].lower() != file2[1].lower():
        sys.exit('Input and output have different extensions')         
    

def check_extension(file):
    
    extensions = ['.jpg', '.jpeg', '.png']
    
    if file in extensions:
        return True
    
    return False
            

if __name__ == '__main__':
    main()