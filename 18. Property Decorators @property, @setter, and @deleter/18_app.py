# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to
# update it, and @price.deleter to delete it.


class Product():
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price_update):
        self._price = price_update

    @price.deleter
    def price(self):
        del self._price


p1 = Product("472")

print(p1.price)

p1.price = "538"

print(p1.price)

del p1.price






