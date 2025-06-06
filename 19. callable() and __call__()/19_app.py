# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an
# input by the factor. Test it with callable() and by calling the object like a function.



class Multiplier():
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, input):
        self.input = input
        return self.factor * self.input
    

m1 = Multiplier(4)

print(callable(m1.__call__))

print(m1(8))







# callable() check karta hai kya koi cheez function ki tarah call ho sakti hai ya nahi.
# __call__() ek aisi method hai jo class ke object ko function banane ki power deti hai.
# Jab aap obj() likhte ho, to actually obj.__call__() run hoti hai.
