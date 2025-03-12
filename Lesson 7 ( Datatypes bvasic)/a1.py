lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]    

lst.remove("a")
print("Updated list :", lst)

lst.pop(4)
print("Updated list :", lst)

lst.reverse()
print("Reversed version of the list :", lst)

lst.sort()
print("Sorted list :", lst)

lst.append("k")
print("Updated list :", lst)

lst = lst[:4]
print("sliced list :", lst)


print("Multiplying list by 2 :", lst*2)


lst.clear()
print("Cleared list :",lst)