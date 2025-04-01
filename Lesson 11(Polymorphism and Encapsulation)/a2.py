class Computer:

    def __init__(self):
        self.maxprice = 999

    def sell(self):
        print("Selling Price: {}".format(self.maxprice))

    def set_max_price(self,price):
        self.maxprice = price


c = Computer()
c.sell()

c.maxprice = 1800
c.sell()

c.set_max_price(1800)
c.sell()



    