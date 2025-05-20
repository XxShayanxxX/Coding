#Program to rreverse string using recursion 
def reversestr(s):

    # if onlty 1 chat remains justr return it 
    if len(s) == 1 : 
        return s[0]
    firstchar = s[0]
    #get the already rversed stringf and add first char to end 
    return reversestr(s[1:]) + firstchar


s = "MOM DAD LOL hi "
print(reversestr(s))