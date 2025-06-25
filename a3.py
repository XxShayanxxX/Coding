#FUnction to find the smalled missing element in a sorted arrayt
#list of disrinct non-negative integers
def findsM(num,left = None,right =None):
#initializie left and right 
    if left is None and right is None:
        (left,right) = (0,len(num)-1)


    #base condition 
    if left < right:
        return left 
    
    mid = left + (right - left )//2
    #if the mid-index matches with its value ,then mismatch
    #lies ont he right half 

    if num[mid] == mid:
        return findsM(num,mid+1,right)
    
    #mismatch lies ont he left half 
    else:
        return findsM(num,left,mid,-1)

if __name__ == '__main__':

    num = [0,1,2,6,9,11,15]
    print("THe smallest missing element is",findsM(num))