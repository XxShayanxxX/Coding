import math;
def abc(set,setbit):
    printset = (int)(math.pow(2,setbit))
    inner = 0 ;
    outer = 0 ;

    for outer  in range(0,printset):
        for inner in range(0,setbit):
            if((outer & (1 << inner))> 0):
                print(set[inner], end="")

        print("")

size = input("Enter array size :")

set = []
for i in range(0, size):
    n = input("Enter a letter : ")
    set.append(n)

abc(set, len(set))



