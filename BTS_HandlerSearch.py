#######################################################################
# Library
import sys
from BTS_HandlerRead import CELLS

#######################################################################
# Globals


#######################################################################
# Functions

# Search and list cells by systems
def handler(list):
    if not list:
        print("List is empty, try to import file first.\n")
    else:
        system = {"LTE": 0, "NR": 0, "GSM": 0, "UMTS": 0, "Other": 0}
        print("Cells by system:")
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
        print(f'LTE cells: {system["LTE"]}\nNR cells: {system["NR"]}\nGSM cells: {system["GSM"]}\nUMTS cells: {system["UMTS"]}\nOther System: {system["Other"]}\n')
    return None

# Search cells by user given parameter with user given value and saves wanted cells in output.txt file
def cellfinder(list):
    temp_cells = []
    filename = open("output.txt", "w", encoding="utf-8")
    filename.write(CELLS.get_variables().replace(" ", "").upper())
    filename.write("\n")
    while(True):
        if not list:
            print("List is empty, try to import file first.\n")
            return None
        else:
            print("Available parameters:",CELLS.get_variables())
            user_input = input("Give parameter and value separated by space, or '0' to exit: ").strip()
            # Check if the user wants to exit
            if user_input == "0":
                break 
            try:
                # Try to split the input into parameter and value
                parameter, value = user_input.split()
            except ValueError:
                # Handle case where input does not split into exactly two parts
                print("Invalid input.\n")
                continue
            
            found = False
            print("\n")
            # Searches cells with user given parameter and value
            for cell in list:
                if getattr(cell, parameter, None) == value:
                    found = True
                    print(f"System: {cell.system}\nSite: {cell.site}\nCell: {cell.cell}\nChannel: {cell.ch}\nCID: {cell.cid}\nPCI: {cell.pci}\nTAC: {cell.tac}\nDirection: {cell.dir}\nLatitude: {cell.lat}\nLongitude: {cell.lon}\nVendor: {cell.vendor}\nRange: {cell.range}\nBeam width: {cell.beam}\nBSIC: {cell.bsic}\nLAC: {cell.lac}")
                    print("\n")
                    temp = [cell.system,cell.site,cell.cell,cell.ch,cell.cid,cell.pci,cell.tac,cell.dir,cell.lat,cell.lon,cell.vendor,cell.range,cell.beam,cell.bsic,cell.lac]
                    temp_cells.append(temp)
            if not found:
                print("Cells not found, try again\n")
                cellfinder(list)
            save = input("Do want to save the search results in file (y/n): ")
            if save == "n":
                print("Search results removed and not save to file.\n")
                temp_cells.clear()
                continue
            elif save == "y":
                print("\n")
                for group in temp_cells:
                    for value in group:
                        filename.write(value)
                        filename.write(",")
                    filename.write("\n")
                    continue
            else:
                print("Invalid selection. Search results removed.\n")
                temp_cells.clear()
                continue
    filename.close()
    return None