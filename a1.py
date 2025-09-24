#Python program to implement queue using array 
#declaring the array of maximum capacity

ar = [0 for _ in range(10)]
n = 10 

#declaring front and rear and intializing both with -1 

front = -1 
rear = -1 

#function to perform enqueue operation 
def enqueue(item):
    #checking overflow condition 
    global n 
    global rear 
    global front 

    if rear == n - 1:
        print("Overflow!", end = " ")
        print("\n", end = " ")
        return 
    
    else:
        #front and rear both are at -1 then 
        #set front and rear at 0 otherwise increment rear 

        if front == -1 and rear == -1 :
            front = 0 
            rear = 0 

        else:
            rear += 1 
            #insterting element at rear 
            ar[rear] = item 
            print("Element inserted")


#function to implement dequeue operation 
def dequeue():
    global n 
    global rear 
    global front 

    #checking underflow condition 
    if front == -1 or front > rear:
        print("Underflow!", end = " ")
        return
    else:
        #if queue is not empty print all the elements from the rear to the front 
        print("Elements are : ",end = "")
        i = front 
        while i <= rear:
            print(ar[i],end = " ")
            print(" ",end = " ")
            i += 1 

        print("\n", end = " ")

def display():
    global n 
    global rear 
    global front 
    #checking whether queue is empty or not 
    if front == -1 :
        #if queue is empty simply return 
        print("Queue is empty", end = " ")
        print("\n", end = " ")
        return
    else:
        #if queue is not empty print all the lements from rear to fornt 
        print("Elements are: ", end = " ")
        i = front
        while i <= rear:
            print(ar[i],end =" ")
            print("",end="")
            i += 1

#function to display front element of queue 
def fronte():
    global n 
    global rear 
    global front 
    #checking whether queue is empty or not 
    if front == - 1:
        #if queue is empty simply return 
        print("Queue is empty", end = " ")

        print("Queue is empty ", end = " ")
        print("\n", end = " ")

        return 
    else: 
        #if queue is not empty print front element 
        print("Front element is:", end = " ")
        print(ar[front],end = " ")
        print("\n",end = " ")

ch = None 
#displaying options of enqueue, dequeue , front , display to the user 

print("1: Intersting element to queue(enqueue)", end = "")
print("\n",end = "")
print("2: Deleting element from the queue(dequeue)", end ="")
print("3: Display front element of queue",end = "")
print("\n", end = " ")
print("4: Display all the elements of queue",end = "")
print("\n", end = "")
print("5:Exit", end = "")
print("\n", end="")
condition = True 

while condition:
    #taking user choice 
    ch = int(input("Enter your choice: "))
    #calling the function accoding to the choice of user 
    if ch == 1:
        item = int(input("Enter element to be inserted: "))
        enqueue(item)

    elif ch == 2:
        dequeue()
    
    elif ch == 3:
        display()  

    elif ch == 4:
        fronte()

    elif ch == 5:
        print("Exit", end = "")
        print("\n", end = " ")

    else:
        print("invalid choice", end = " ")
        print('\n',end = " ")

    condition = ch!=5 
