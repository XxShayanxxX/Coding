class node:
    def __init__(self,data):
        self.data = data 
        self.prev = None   #adress of the previous node 
        self.next = None   #adress of the next node 


class DoubleLL:
    def  __init__(self):
        self.head = None


    def insetbeg(self,data):
        nb = node
        nb.next = self.head

        self.head = nb 


    def insertend(self,data):
        ne = node(data)
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = ne
        ne.prev = temp

    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head 
            while temp:
                print(temp.data,"--->", end=' ')

                temp = temp.next


#Drivers code 

l = DoubleLL()
n = node(10)
l.head = n 
n1 = node(20)
n.next = n1
n2 = node(30)
n1.prev = n2 
n1.next = n
l.display()
print(end ="\n")
l.insertbeg(100)
l.display()
print(end = "\n")
l.insert_end(100)
l.display()


    
