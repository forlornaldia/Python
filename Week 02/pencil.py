import time
import os  

pencil_1 = '''         

                                     ^
                                    /%\ 
                                   /   \ 
                                  /     \ 
                                 /_______\ 
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |  No.2   |
                                |         |
                                !!!!!!!!!!!
                                !!!!!!!!!!!
                                @@@@@@@@@@@
                                @@@@@@@@@@@
                                @@@@@@@@@@@ '''

pencil_2 = '''           
                                    __         
                                     ^
                                    /%\ 
                                   /   \ 
                                  /     \ 
                                 /_______\ 
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |  No.2   |
                                |         |
                                !!!!!!!!!!!
                                !!!!!!!!!!!
                                @@@@@@@@@@@
                                @@@@@@@@@@@
                                @@@@@@@@@@@ '''

pencil_3 = '''           
                                  ____         
                                     ^
                                    /%\ 
                                   /   \ 
                                  /     \ 
                                 /_______\ 
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |  No.2   |
                                |         |
                                !!!!!!!!!!!
                                !!!!!!!!!!!
                                @@@@@@@@@@@
                                @@@@@@@@@@@
                                @@@@@@@@@@@ '''

pencil_4 = '''           
                                ______         
                                     ^
                                    /%\ 
                                   /   \ 
                                  /     \ 
                                 /_______\ 
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |  No.2   |
                                |         |
                                !!!!!!!!!!!
                                !!!!!!!!!!!
                                @@@@@@@@@@@
                                @@@@@@@@@@@
                                @@@@@@@@@@@ '''

pencil_5 = '''           
                              ________         
                                     ^
                                    /%\ 
                                   /   \ 
                                  /     \ 
                                 /_______\ 
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |         |
                                |  No.2   |
                                |         |
                                !!!!!!!!!!!
                                !!!!!!!!!!!
                                @@@@@@@@@@@
                                @@@@@@@@@@@
                                @@@@@@@@@@@ '''

def animate():
    time.sleep(.4)
    os.system('cls||clear')

condEE = "0"

def draw():
    print(f"{pencil_1}")
    animate()
    print(f"{pencil_2}")
    animate()
    print(f"{pencil_3}")
    animate()
    print(f"{pencil_4}")
    animate()
    print(f"{pencil_5}")
    animate()

if condEE == "0":
    draw()

def eloop():
    print(f"{pencil_4}")
    animate()
    print(f"{pencil_3}")
    animate()
    print(f"{pencil_4}")
    animate()
    print(f"{pencil_3}")
    animate()
    eloop()


eloop()