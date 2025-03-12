def test(lst):
    dictonary = {}
    for items in lst : 
        dictonary[items[0]] = items[1:]

students = [[1, "John" , "Doe"], [2, "Jane", "Smith"], [3, "Jack", "Jones"], [4, "Jill", "Roberts"]]    

print("\n Original list of students : " , students) 
print(students)

print("\n converted to a dictionary : ")
print(test(students))


    
        
    