#build in function
def compare(n1,n2):
    return str(n1) + str(n2) + str(n1)

#section sort 
def largestnumber(nums):
    for i in range(len(nums),0,-1):
        tmp = 0 
        for j in range(i):
            if not compare(nums[j],nums[tmp]):
                tmp = j 
            nums[tmp],nums[i-1] = nums[i-1],nums[tmp]
        return str(int("".join(map(str,nums))))
    

#Drivers code 
arr = [3,30,34,5,12]
print("given array : ",arr)
print("Largest possible number :",largestnumber(arr))