######################################################################
# Creator: Antti Suomela
# Handling BTS information
#######################################################################
# Globals

import BTS_HandlerRead
import BTS_HandlerSearch

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
            list = BTS_HandlerRead.read(list)
        elif (selection == 2):
            BTS_HandlerSearch.handler(list)
        elif (selection == 3):
            BTS_HandlerSearch.cellfinder(list)
        else:
            print("Invalid selection, try again...")
            
    list.clear()

#eof