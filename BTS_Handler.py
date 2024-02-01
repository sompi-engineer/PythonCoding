######################################################################
# Creator: Antti Suomela
# Date: 13.1.2024 (original version)
# Version 1: 21.1.2024
# Version 2: 29.1.2024
# Handling of BTS information
#######################################################################
# Globals

import BTS_HandlerLibrary

#######################################################################
# Main program

if __name__ == "__main__":
    list = []
    while (True):
        print("\nOptions")
        print("1) Read BTS file content (.txt)")
        print("2) Shows the number of cells in systems")
        print("3) Find cell information")
        print("0) Exit")
        print("\n")
        selection = int(input("Select function: "))
        print("\n")
        if (selection == 0):
            break
        elif (selection == 1):
            list = BTS_HandlerLibrary.read(list)
        elif (selection == 2):
            BTS_HandlerLibrary.handler(list)
        elif (selection == 3):
            BTS_HandlerLibrary.cellfinder(list)
        else:
            print("Invalid selection, try again...")
            
    list.clear()


#eof