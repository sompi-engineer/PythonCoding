######################################################################
# Creator: Antti Suomela
# Date: 13.1.2024 (original version)
# Version 1: 21.1.2024
# Handling of BTS information
#######################################################################
# Globals

SEPARATOR = ","

import sys

class CELLS:
    system = ""
    site = ""
    cell = ""

REQUIRED_PARAMETERS = ['SYSTEM', 'CELL', 'SITE']

#######################################################################
# Subprograms

def read(list):
    filename = input("Enter the file name and path: ")
    header_list = []
    system_no = 0
    site_no = 0
    cell_no = 0
    number = 0
    try:
        file = open(filename, "r", encoding="utf-8")
        header_list = file.readline().split(SEPARATOR)[:-1]           # read header line, split parameters with SEPARATOR and leave line change out
        print("File contains following parameters: ", header_list, "\n")
        # Check that file contains the required parameters, if not exit the program
        if all(element in header_list for element in REQUIRED_PARAMETERS):
            pass
        else:
            print("Missing mandatory parameters {0}, closing...".format(REQUIRED_PARAMETERS))
            sys.exit()
        # Resolve which column number contains required parameters
        for parameter in header_list:
            if parameter == "SYSTEM":
                system_no = number
            elif parameter == "SITE":
                site_no = number
            elif parameter == "CELL":
                cell_no = number
            number += 1
        # Read through the file and append wanted values to class
        while True:
            line = file.readline()[:-1]         # leave line change out of the read
            if (len(line) == 0):
                break
            column = line.split(SEPARATOR)
            cell = CELLS()
            cell.system = column[system_no]
            cell.site = column[site_no]
            cell.cell = column[cell_no]
            list.append(cell)
        file.close()
    except Exception:
        print("Problem with file handling, closing...")
        sys.exit()
    #print("File read successfully.\n")
    return list

def handler(list):
    system = {"LTE": 0, "NR": 0, "GSM": 0, "UMTS": 0, "Other": 0}
    for cell in list:
        if cell.system == "LTE":
            system["LTE"] += 1
        elif cell.system == "NR":
            system["NR"] += 1
        elif cell.system == "GSM":
            system["GSM"] += 1
        elif cell.system == "UMTS":
            system["UMTS"] += 1
        else:
            system["Other"] += 1
    print("LTE cells: {0}\nNR cells: {1}\nGSM cells: {2}\nUMTS cells: {3}\nOther System: {4}\n".format(system["LTE"],system["NR"],system["GSM"],system["UMTS"],system["Other"]))
    return

def main():
    list = []
    list = read(list)
    handler(list)
    return None


#######################################################################
# Main program

main()
          
#eof