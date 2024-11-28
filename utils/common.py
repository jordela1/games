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

def menu_maker(menu_title: str, menu_desc) -> str:
    max_menu_len = 50
    menu_title_len = len(menu_title)
    menu_desc_len = len(menu_desc)
    menu_desc_rows = []

    # If the length of the provided title is < the default max, 
    # but is odd will append a space to make the buffers even on either side
    # If the provided title is greater than default max will set the default max to that length
    if menu_title_len < max_menu_len and menu_title_len % 2 != 0:
        menu_title + " "
    elif menu_title_len > max_menu_len:
        max_menu_len = menu_title_len

    # If the length of the provided desc is > the current max will split into rows of that length
    if menu_desc_len > max_menu_len:
        menu_desc_list = menu_desc.split()
        w




