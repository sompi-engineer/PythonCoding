######################################################################
# Creator: Antti Suomela
# Date: 13.1.2024 (original version)
# Version 1: 21.1.2024
# Handling of BTS information
#######################################################################
# Globals

import BTS_HandlerLibrary

#######################################################################
# Subprograms

def main():
    list = []
    list = BTS_HandlerLibrary.read(list)
    BTS_HandlerLibrary.handler(list)
    list.clear()
    return None

#######################################################################
# Main program

main()
          
#eof