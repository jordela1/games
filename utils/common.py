# common python utilities

def said_yes( question: str ) -> bool:
    
    while True:
        response = input(f"> {question}? (yes/no): ")
        if response == "y" or response == "yes":
            return True
        elif response == "n" or response == "no":
            return False
        else:
            print("Incorrect response, please enter 'yes/y' or 'no/n'")
