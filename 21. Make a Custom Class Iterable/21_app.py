# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make
# the object iterable in a for-loop, counting down to 0.


class CountUpToThree():
    def __init__(self):
        self.counter = 1


    def __iter__(self):             # The Iterator Starter
        return self
    
    
    def __next__(self):             # The Next Value Provider (Each time the for loop needs a new value, Python calls this method.)
        if self.counter <= 3:
            current = self.counter
            self.counter += 1
            return current
        else:
            raise StopIteration
        
for numbers in CountUpToThree():
    print(numbers)





class CountDown():
    def __init__(self, start):  # The Iterator Starter
        self.start = start


    def __iter__(self):
        return self
    

    def __next__(self):      # The Next Value Provider (Each time the for loop needs a new value, Python calls this method.)
        if self.start >= 0:
            curr_val = self.start
            self.start -= 1
            return curr_val
        else:
            raise StopIteration
        

count = CountDown(5)


for nums in count:
    print(nums)

