# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during
# initialization. Access a method of the Engine class via the Car class.


class Engine():
    
    

    def start(self):
        return "A car has an Engine"



class Car():
    def __init__(self, object_engine):
        self.engine = object_engine

    def drive(self):
        print(f"{self.engine.start()}")


car1 = Car(Engine())
car1.drive()









