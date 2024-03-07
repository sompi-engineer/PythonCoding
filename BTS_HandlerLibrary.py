#######################################################################
# Library
#######################################################################
# Globals
import sys

SEPARATOR = ","

class CELLS:
    system = ""
    site = ""
    cell = ""
    ch = 0
    cid = 0
    pci = 0
    tac = 0
    dir = 0
    lat = 0
    lon = 0
    vendor = ""
    range = 0
    beam = 0
    bsic = 0
    lac = 0

REQUIRED_PARAMETERS = ['SYSTEM', 'CELL', 'SITE']

#######################################################################
# Functions

# Read given txt file, take header information and stores cell information to class
def read(list):
    filename = input("Enter the file name and path: ")
    header_list = []
    parameter_no = {"system_no": 0, "site_no": 0, "cell_no": 0, "ch_no": 0, "cid_no": 0, "pci_no": 0, "tac_no": 0, "dir_no": 0, "lat_no": 0, "lon_no": 0, "vendor_no": 0, "range_no": 0, "beam_no": 0, "bsic_no": 0, "lac_no":0}
    number = 0
    try:
        file = open(filename, "r", encoding="utf-8")
        header = file.readline()[:-1]                   # read header line
        header_list = header.split(SEPARATOR)           # split parameters with SEPARATOR and store to list
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
                parameter_no["system_no"] += number
            elif parameter == "SITE":
                parameter_no["site_no"] += number
            elif parameter == "CELL":
                parameter_no["cell_no"] += number
            elif parameter == "CH":
                parameter_no["ch_no"] += number
            elif parameter == "CID":
                parameter_no["cid_no"] += number
            elif parameter == "PCI":
                parameter_no["pci_no"] += number
            elif parameter == "TAC":
                parameter_no["tac_no"] += number
            elif parameter == "DIR":
                parameter_no["dir_no"] += number
            elif parameter == "LAT":
                parameter_no["lat_no"] += number
            elif parameter == "LON":
                parameter_no["lon_no"] += number
            elif parameter == "VENDOR":
                parameter_no["vendor_no"] += number
            elif parameter == "RANGE":
                parameter_no["range_no"] += number
            elif parameter == "BEAM":
                parameter_no["beam_no"] += number
            elif parameter == "BSIC":
                parameter_no["bsic_no"] += number
            elif parameter == "LAC":
                parameter_no["lac_no"] += number
            number += 1
        # Read through the file and append wanted values to class
        while True:
            line = file.readline()[:-1]         # leave line change out of the read
            if (len(line) == 0):
                break
            column = line.split(SEPARATOR)
            cell = CELLS()
            cell.system = column[parameter_no["system_no"]]
            cell.site = column[parameter_no["site_no"]]
            cell.cell = column[parameter_no["cell_no"]]
            cell.ch = column[parameter_no["ch_no"]]
            cell.cid = column[parameter_no["cid_no"]]
            cell.pci = column[parameter_no["pci_no"]]
            cell.tac = column[parameter_no["tac_no"]]
            cell.dir = column[parameter_no["dir_no"]]
            cell.lat = column[parameter_no["lat_no"]]
            cell.lon = column[parameter_no["lon_no"]]
            cell.vendor = column[parameter_no["vendor_no"]]
            cell.range = column[parameter_no["range_no"]]
            cell.beam = column[parameter_no["beam_no"]]
            cell.bsic = column[parameter_no["bsic_no"]]
            cell.lac = column[parameter_no["lac_no"]]
            list.append(cell)
        file.close()
    except Exception:
        print("Problem with file handling, closing...")
        sys.exit()
    #print("File read successfully.\n")
    return list

# Search and list cells by systems
def handler(list):
    if (len(list) == 0):
        print("List is empty, try to import file first\n")
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
        print("LTE cells: {0}\nNR cells: {1}\nGSM cells: {2}\nUMTS cells: {3}\nOther System: {4}\n".format(system["LTE"],system["NR"],system["GSM"],system["UMTS"],system["Other"]))
    return None

def cellfinder(list):
    findSite = input("Give site name to search: ")
    for cell in list:
        if cell.site == findSite:
            print("System: {0}\nSite: {1}\nCell: {2}\nChannel: {3}\nCID: {4}\nPCI: {5}\nTAC: {6}\nDirection: {6}\nLatitude: {7}\nLongitude: {8}\nVendor: {9}\nRange: {10}\nBeam width: {11}\nBSIC: {12}\nLAC: {13}\n".format(cell.system,cell.site,cell.cell,cell.ch,cell.cid,cell.pci,cell.tac,cell.dir,cell.lat,cell.lon,cell.vendor,cell.range,cell.beam,cell.bsic,cell.lac))
    return None