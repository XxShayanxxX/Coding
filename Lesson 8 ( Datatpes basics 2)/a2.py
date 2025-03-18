my_set = {1,2,3,4,5}

my_set.add(6)
print(my_set)

set1 = my_set
set2 = {1,2,3,3,3,3,3,3,4,4,4,5}

print(set1)
print(set2)
print(set1.union(set2))
print(set1.difference(set2))   
print(set1.symmetric_difference(set2))

print(set2.difference(set1))   
print(set2.symmetric_difference(set1))

