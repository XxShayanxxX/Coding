#Program to find HCF/LCM

#ENTER 2 NUMBERS

numberlargest = int(input("Enter largest number:"))
numbersmallest = int(input("Enter smallest number:"))
# Using Eulclidens algorithm to find HCF

while numbersmallest != 0:
    numberstore = numbersmallest
    numbersmallest = numberlargest % numbersmallest
    numberlargest = numberstore

#Output !!!
print("HCF is:", numberlargest)
