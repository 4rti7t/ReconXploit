import sys
import os

# Clear screen function
def clear_screen():
    # For Windows
    if sys.platform == "win32":
        os.system('cls')
    # For Linux and macOS
    else:
        os.system('clear')

# Call the function to clear the screen
clear_screen()

# Rest of your script goes here
    

# ----- Logo and Header -----
def print_header():
    logo = """
    
   ▄████████    ▄████████  ▄████████  ▄██████▄  ███▄▄▄▄   ▀████    ▐████▀    ▄███████▄  ▄█        ▄██████▄   ▄█      ███     
  ███    ███   ███    ███ ███    ███ ███    ███ ███▀▀▀██▄   ███▌   ████▀    ███    ███ ███       ███    ███ ███  ▀█████████▄ 
  ███    ███   ███    █▀  ███    █▀  ███    ███ ███   ███    ███  ▐███      ███    ███ ███       ███    ███ ███▌    ▀███▀▀██ 
 ▄███▄▄▄▄██▀  ▄███▄▄▄     ███        ███    ███ ███   ███    ▀███▄███▀      ███    ███ ███       ███    ███ ███▌     ███   ▀ 
▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███        ███    ███ ███   ███    ████▀██▄     ▀█████████▀  ███       ███    ███ ███▌     ███     
▀███████████   ███    █▄  ███    █▄  ███    ███ ███   ███   ▐███  ▀███      ███        ███       ███    ███ ███      ███     
  ███    ███   ███    ███ ███    ███ ███    ███ ███   ███  ▄███     ███▄    ███        ███▌    ▄ ███    ███ ███      ███     
  ███    ███   ██████████ ████████▀   ▀██████▀   ▀█   █▀  ████       ███▄  ▄████▀      █████▄▄██  ▀██████▀  █▀      ▄████▀   
  ███    ███                                                                           ▀                                     
                                       \033[1mразработано @ARTIST для INFLUXION\033[0m
    """
