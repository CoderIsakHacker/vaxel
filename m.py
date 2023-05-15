import os
import vaxlare

def main():
    os.system("cls" if os.name == "nt" else "clear")
    
    print("\n\t-Växlare-\n")

    pris = input("\tMata in pris på varan i kr: ")
    inbet = input("\tMata in inbetalt belopp i kr: ")
    #anropar växlings funktion

    exChangeNow(int(pris), int(inbet))

def exChangeNow(priset, inbetalning):

    if priset > inbetalning:
        print("\n\t Mer pengar tack! ")

    else:

        vaxel_tillbaka_dictionary = vaxlare.get_exchange_dict(inbetalning, priset)

        print("\n\t------------------------------------------------------------------")
        print("\tVäxel tillbaka:\n")
        print("\tAntal 500 lappar: " + str(vaxel_tillbaka_dictionary[500]))
        print("\tAntal 100 lappar: " + str(vaxel_tillbaka_dictionary[100]))
        print("\tAntal 50 lappar: " + str(vaxel_tillbaka_dictionary[50]))
        print("\tAntal 20 lappar: " + str(vaxel_tillbaka_dictionary[20]))
        print("\tAntal 10 kronor: " + str(vaxel_tillbaka_dictionary[10]))
        print("\tAntal 5 lappar: " + str(vaxel_tillbaka_dictionary[5]))
        print("\tAntal 1 kronor: " + str(vaxel_tillbaka_dictionary[1]))



main()