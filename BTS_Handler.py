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
        
        if all(element in header_list for element in REQUIRED_PARAMETERS):
            pass
        else:
            print("Missing mandatory parameters {0}, closing...".format(REQUIRED_PARAMETERS))
            sys.exit()

        for parameter in header_list:
            if parameter == "SYSTEM":
                system_no = number
            elif parameter == "SITE":
                site_no = number
            elif parameter == "CELL":
                cell_no = number
            number += 1

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
    LTE = 0
    NR = 0
    Other = 0
    GSM = 0
    for cell in list[1:]:       # leave header row out
        if cell.system == "LTE":
            LTE += 1
        elif cell.system == "NR":
            NR += 1
        elif cell.system == "GSM":
            GSM += 1
        else:
            Other += 1
    print("LTE cells: {0}\nNR cells: {1}\nGSM cells: {2}\nOther System: {3}\n".format(LTE,NR,GSM,Other))
    return

def main():
    list = []
    list = read(list)
    handler(list)
    #for cell in list:
      #  print("System: ", cell.system)
    #print(list[0].system)


    return None


#######################################################################
# Main program

main()
          
#eof