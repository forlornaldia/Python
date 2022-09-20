import os
from time import sleep
def clrcon():
    # Windarr
    if os.name == "nt":
        return os.system('cls')

    # Macnchz + LinusTT
    else:
        return os.system('clear')
clrcon()