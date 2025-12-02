import sys 

#Structure for the elements in the priority queue
class item:
    value = 0 
    priority = 0 

class GFG:

    #STore elemenet of a priority queue queue
    pr = [None] * (100000)

    #Pointer to the last index 
    size = -1
    #FUnction to insert a new element into priority queue
    @staticmethod
    def enqueue(value,priority):
        
        #Increase the size 
        GFG.size +=1 

        #Insert element
        GFG.pr[GFG.size] = item()
        GFG.pr[GFG.size].value = value 
        GFG.pr[GFG.size].priority = priority


    #FUnction to check the top element 
    @staticmethod
    def peek():
        highestPriority = -sys.maxsize
        ind = -1


    #Check for the element with highest priority 
        i = 0 
        while (i <= GFG.size):
        
        #If priority is same choose
        #the element with the higher value 

            if(highestPriority == GFG.pr[i].priority and ind > -1 and GFG.pr[ind].value < GFG.pr[i].value):
               highestPriority = GFG.pr[i].priority
               ind = i 

            elif(highestPriority < GFG.pr[i].priority):
                highestPriority = GFG.pr[i].priority
                ind = 1 

            i += 1 
        #Retrnposition of the element 
        return ind 

        #FUnction to remove the elemenr wirh the highest priority 
    @staticmethod
    def dequeue():

        #Find the position of the element with the highestr priority 

        ind = GFG.peek()
        #Shift the element one index before 
        #the position from the highest priority element is found 

        i = ind 
        while(i < GFG.size):
            GFG.pr[i] = GFG.pr[i + 1]
            i += 1 

        #Decrease the size of the 
        #priority queue by one 


    @staticmethod 
    def main(args):

        #Function call to insert elements as per priority 

        GFG.enqueue(10,2)
        GFG.enqueue(14,4)
        GFG.enqueue(16,4)
        GFG.enqueue(12,3)

        #Stores the top element 
        # at the moment 

        ind = GFG.peek()
        print(GFG.pr[ind].value)


        #Dequeue the top element 
        GFG.dequeue()

        #Chekc the top element
        ind = GFG.peek()
        print(GFG.pr[ind].value)


        #Dequeue the top element  
        GFG.dequeue()

        #Check the top element    
        ind = GFG.peek()
        print(GFG.pr[ind].value) 

        #Dequeue the top element 
        GFG.dequeue()

        #CHeck the top element 
        ind = GFG.peek()  
        print(GFG.pr[ind].value)

if __name__ == "__main__":
    GFG.main([])



