#***************************************************LINKED LIST****************************************
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self,data):
        new_node = node(data)   #node used
        cur = self.head   #constructor used
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print("\n",elems)
        
my_list = linked_list()                               
    
    #***************************************************TRIO-MUSIC-PLAYER****************************************
#***************************************************HOME****************************************
def quickplay():
    #defination
    print("\n played...")
    home()
def openlist():
    #defination
    my_list.display()
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
    elif action==5:
        songname=input("Enter songname: ")
        my_list.append(songname)
    else:
        print("\n*** Invalid input ***\n")
    home()

print("                    *-------TRIO-------*")
print("                    *   MUSIC PLAYER   *")
home()
