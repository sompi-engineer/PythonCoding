######################################################################
# Creator: Antti Suomela
# Date: 13.1.2024
# Handling of BTS information
#######################################################################
# Globals

SEPARATOR = ","

import sys

class CELLS:
    system = ""
    site = ""
    cell = ""


#######################################################################
# Subprograms


def read(list):
    filename = input("Enter the file name and path: ")
    try:
        file = open(filename, "r", encoding="utf-8")
        while True:
            line = file.readline()[:-1]         # leave line change out of the read
            if (len(line) == 0):
                break
            column = line.split(SEPARATOR)
            cell = CELLS()
            cell.system = column[0]
            cell.site = column[1]
            cell.cell = column[2]
            list.append(cell)
        file.close()
    except Exception:
        print("Problem with file handling, closing...")
        sys.exit()
    print("File read successfully.")
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
    print("LTE cells: {0}\nNR cells: {1}\nGSM cells: {2}\nOther System: {3}".format(LTE,NR,GSM,Other))



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