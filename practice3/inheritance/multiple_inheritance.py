class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):#duck inherits methods from both flyer and swimmer
    pass

d = Duck()
d.fly()    # Flying
d.swim()   # swimming

