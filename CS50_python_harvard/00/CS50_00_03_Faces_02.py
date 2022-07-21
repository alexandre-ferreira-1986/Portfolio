# Function Convert Faces
def convert(text):
    text1 = text.replace(":)", "🙂")
    text2 = text1.replace(":(", "🙁")
    return text2
        
# Function Main
def main():
    text = input("Message: ")
    converted = convert(text)
    print(converted)
    
# Starting the main function    
main()