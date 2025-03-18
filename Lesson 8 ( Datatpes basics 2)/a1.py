mytuple = ()
print(mytuple)

mytuple = (1,2,3,4,5)
print(mytuple)

mytuple = ("Hello" , 1 , 2 , "Hi")
print(mytuple)

mytuple = ("mouse" , [1,1,1,8], [1,2,3,4,])
print(mytuple[0][1])

mytuple = (1,2,3,4,5,7,8,8,9,10.12,13,14,15,16,17,18,19,20)
print([0])
print([5])


tuple2 = ("mouse" , [1,1,1,8], [1,2,3,4,])
print(tuple2[1][2])

print("slicing : " , tuple2[0:2])   

for letter in tuple2:
    print(letter)