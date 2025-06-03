#Program to find all the possible combinations when we press keys in phone keypad

keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def printC(combinations, curr , output,n):
    if(curr == n):
        print(*output,sep="," )
        return 
# Print all the possible combination bny itterating first 1 to 3 for number an finding that index in keypad
    for i in range(len(keypad[combinations[curr]])):
        output.append(keypad[combinations[curr]][i])


        printC(combinations,curr + 1, output,n)
        output.pop()
        if(combinations[curr]==0 or combinations[curr]==1):
            return
combinations = [4,3,4]
n = len(combinations)
printC(combinations,0,[],n)
