class fruit:

    def __init__(self):
        print("Fruit created")


    def __del__(self):
        print("Fruit deleted")


obj = fruit()
del obj