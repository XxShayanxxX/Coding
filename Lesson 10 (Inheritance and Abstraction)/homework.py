from math import tan, pi 
n_sides = int(input("Input the numebr of sides:"))
s_lenght = float(input("Input the length of a side:"))
p_area = n_sides * (s_lenght ** 2) / (4 * tan(pi / n_sides))
print("the area of the polygon is:", p_area)