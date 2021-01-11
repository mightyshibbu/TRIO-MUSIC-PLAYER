# TRIO-MUSIC-PLAYER
Programme to illustrate the basic use of data structure.
import random


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self):
        data=input("Enter songname: ")
        new_node = node(data)  # node used
        cur = self.head  # constructor used
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        print("Song added successfully!")
        a = input("Press 5 to add more or press any key to return Home: ")
        if a != '5':
            home()
        else:
            my_list.append()

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        j = 1
        for i in elems:
            print("\n", j, ".", i)
            j = j + 1

    def checkempty(self):
        cur_node = self.head
        if cur_node.next == None:
            return (True)
        else:
            return (False)

    def quickplaylist(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        leng = my_list.length()

        ran = random.randint(0, leng - 1)

        print("\n\tCurrently playing: ", elems[ran])
         from time import sleep
               playlist = 'SONGNAME.............'
                for i in range(20):
                    print(playlist[i],  end='-'); sleep(0.5) #delayfunction

    def alternate(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        leng = my_list.length()
        for i in range(0, leng):
            print("\nCurrently playing: ", i+1, ".", elems[i])
        from time import sleep
             playlist = 'SONGNAME.............'
              for i in range(20):
                print(playlist[i],  end='-'); sleep(0.5)#delayfunction
        if i == leng - 1:
            print("\n************PLAYLIST_PLAYED************")

    def loop(self):
        print("'Select the number of a song from the playlist: '")
        my_list.display()
        s=int(input())
        n=int(input("Enter no. of times you want to this song to play: "))
        cur_node = self.head
        for p in range(s):
            cur_node=cur_node.next
        for i in range(n):
            print("\nPlaying ",cur_node.data)
            from time import sleep
                 playlist = 'SONGNAME.............'
                 for i in range(20):
                        print(playlist[i],  end='-'); sleep(0.5) #delayfunction

    def shuffle(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        leng = my_list.length()
        again=0
        while True:
            ran = random.randint(0, leng - 1)
            print("\n\tCurrently playing: ", elems[ran])
             from time import sleep
                playlist = 'SONGNAME.............'
                for i in range(20):
                     print(playlist[i],  end='-'); sleep(0.5)#delayfunction
            again=input("\n\tPress E to Stop:")
            if again=="e" or again=="E":
                break

my_list = linked_list()


# ***************************************************TRIO-MUSIC-PLAYER****************************************
# ***************************************************HOME****************************************
def quickplay():
    # defination
    print("*******************************************************")
    if my_list.checkempty() == True:
        print("Play list is Empty ! \n Add songs by pressing 5")
    else:
        print("\nHere you go !\n")
        my_list.quickplaylist()
    print("*******************************************************")
    home()


def openlist():
    # defination
    print("\n**************PLAYLIST*************")
    my_list.display()
    print("\n*************************************")
    home()


def changesequence():
    # defination
    print("*******************************************************")
    opt = int(input("\nSequence options:\n1. Alternate\n2. Loop\n3. Shuffle \n\n Enter option: "))
    if opt == 1:
        my_list.alternate()
    elif opt == 2:
        my_list.loop()
    elif opt == 3:
        my_list.shuffle()
    else:
        print("Error! Enter valid input: ")
        changesequence()

    home()


def home():
    print("*******************************************************")
    print("\nHOME: (Press respective number to perform action)")
    print("\n1. Quick start", "\n2. Open list", "\n3. Sequence [Alternate/Loop/Shuffle]", "\n4. Exit", "\n5. Add songs")

    action = input("Select operation number:")

    if action == "4":
        print("\nExiting TMP player...")
        exit()
    elif action == "1":

        quickplay()
    elif action == "2":
        print("\nHere's the List:\n")
        openlist()
    elif action == "3":
        changesequence()
    elif action == "5":
        my_list.append()


    else:
        print("\n*** Invalid input ***\n")
    home()

