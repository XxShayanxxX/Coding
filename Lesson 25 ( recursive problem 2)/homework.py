total_amount = int(input('Enter a number : '))
listofnotes = [1000,500,100,50,20,10,5]

for i in listofnotes:
    numofnotes = total_amount // i
    total_amount %= i 
    if numofnotes != 0:
        print(f"The number of notes of {i} is {numofnotes}")