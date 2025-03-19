class parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


blue =  parrot("water", 10)
argon = parrot("fire", 17)

print("bkue is a {}".format(blue.species))
print("argon is a {}". format(argon.species))

print("{} is  {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(argon.name, argon.age))