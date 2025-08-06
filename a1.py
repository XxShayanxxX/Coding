class node:
    def __init__(self,data):
        self.data = data 
        self.next = None #adress of the next node 

        
class singlyLL:
    def __init__(self):
        self.head = None

    #swap will swap the given two nodes 
    def swap(self,n1,n2):
        prevNode1 = None;
        prevNode2 = None;
        node1 = self.head;
        node2 = self.head;

        #checks if list is empty 
        if(self.head == None):
            return;

        #if n1 and n2 are equal, then list will reamin the same 
        if(n1 == n2):
            return; 

        #SSearch for node 1 
        while(node1 != None and node1.data != n1):
            prevNode1 = node1;
            node1 = node1.next;

        #SSearch for node 2 
        while(node2 != None and node2.data != n2 ):
            prevNode2 = node2
            node2 = node2.next;

        if(node1 != None and node2 != None):

#if previous node to nodel is not none then, it will point to node2 
            if(prevNode1 != None):
                prevNode1.next = node2 

            else:
                print("Swapping is not possible")

    def display(self):
        if self.head == None:
                print("List is empty")

        else: 
            temp = self.head 
            while temp:
                print(temp.data,"---->",end = " ")
                temp = temp.next

#drivers code 
l = singlyLL()
n = node(10)
l.head = n
n1 = node(20)
n.next = n1 
n2 = node(30)
n1.next = n2 
n3 = node(40)
n2.next = n3 
l.display()
print(end ='\n')
l.swap(10,30)
l.display()


            