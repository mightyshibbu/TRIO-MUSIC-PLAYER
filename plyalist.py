# TRIO-MUSIC-PLAYER
Programme to illustrate the basic use of data structure.
class CircularQueue(): 
   
    def _init_(self, size):  
        self.size = size 
          
        self.queue = [None for i in range(size)]  
        self.front = self.rear = -1
  
    def enqueue(self, data): 
           
        if ((self.rear + 1) % self.size == self.front):  
            print(" Queue is Full\n") 
               
        elif (self.front == -1):  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data 
        else: 
              
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = data 
              
    def dequeue(self): 
        if (self.front == -1):
            print ("Queue is Empty\n") 
            
        elif (self.front == self.rear):  
            temp=self.queue[self.front] 
            self.front = -1
            self.rear = -1
            return temp 
        else: 
            temp = self.queue[self.front] 
            self.front = (self.front + 1) % self.size 
            return temp 
  
    def display(self): 
       
        if(self.front == -1):  
            print ("Queue is Empty") 
  
        elif (self.rear >= self.front): 
            print("Elements in the circular queue are:",  
                                              end = " ") 
            for i in range(self.front, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        else: 
            print ("Elements in Circular Queue are:",  
                                           end = " ") 
            for i in range(self.front, self.size): 
                print(self.queue[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        if ((self.rear + 1) % self.size == self.front): 
            print("Queue is Full") 
   
ob = CircularQueue(5) 
ob.enqueue(7) 
ob.enqueue(8) 
ob.enqueue(9) 
ob.enqueue(10) 
ob.display() 
print ("Deleted value = ", ob.dequeue()) 
print ("Deleted value = ", ob.dequeue()) 
ob.display() 
ob.enqueue(11) 
ob.enqueue(12) 
ob.enqueue(5) 
ob.display()
