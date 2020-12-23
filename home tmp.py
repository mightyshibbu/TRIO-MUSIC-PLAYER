                                                  #TRIO-MUSIC-PLAYER

def quickplay():
    #defination
    print("\n played...")
    home()
def openlist():
    #defination
    print("\nList displayed!")
    home()
def changesequence():
    #defination
    print("\nSEQ options...")
    home()


def home():
    print("\nHOME: (Press respective number to perform action)")
    print("\n1. Quick start","\n2. Open list","\n3. Sequence [Alternate/Loop/Shuffle]","\n4. Exit")
    
    action=int(input("Select operation number:"))

    if action==4:
        print("\nExiting TMP player...")
        exit()
    elif action==1:
        print("\nHere you go !\n")
        quickplay()
    elif action==2:
        print("\nHere's the List:\n")
        openlist()
    elif action==3:
        changesequence()
    else:
        print("\n*** Invalid input ***\n")
        home()

print("                    *-------TRIO-------*")
print("                    *   MUSIC PLAYER   *")
home()
