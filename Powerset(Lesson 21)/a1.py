import math;
def printPowerset(set,setSize):
    # Find total elements possible in the power set 
    printPowerset = (int) (math.pow(2,setSize));
    outer = 0;
    inner = 0;

    for outer in range(0,printPowerset):
        for inner in range(0,setSize):
            #Check if inner bit in the outer is set If set then print inner element from set
            if((outer & (1 << inner)) > 0):
                print(set[inner],end ="")

        print("")

size = int(input("Enter array size"))

set = []
for i in range(0,size):
    n = int(input("enter elements : "))
    set.append(n)

printPowerset(set,len(set))
