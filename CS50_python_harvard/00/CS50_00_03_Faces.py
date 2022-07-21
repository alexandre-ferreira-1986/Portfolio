# Function Convert Faces
def convert(text):
    if text == ":)":
        return "🙂"
    elif text == ":("
        
# Function Main
def main():
    text = input("Message: ")
    converted = convert(text)
    print(converted)
    
# Starting the main function    
main()