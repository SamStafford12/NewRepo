class Animal:

    def __init__(self,name):
        self.name = name

    def add_weight(self,weight):
        self.weight = weight

    def add_noise(self,noise):
        self.noise = noise

    def returnmethod(self):
        return"xyz"

class Dog(Animal):
    
    def __init__(self, name, vocalization='bark'):
        super().__init__(name)
        self.vocalization = vocalization

    def speak(self):
        return "bark"
        #print("woof woof bark")

class Cat(Animal):
    
    def __init__(self, name, vocalization='Meow'):
        super().__init__(name)
        self.vocalization = vocalization
        
x = Dog("Doggo")
x.add_weight(12)
x.add_noise('bark')
s = x.returnmethod()
print(s)
print(x.weight)
print(x.noise)
print(x.vocalization)
print(x)
c = Cat("Furry")
c.add_weight(8)
c.add_noise('meow')
v = c.returnmethod()
print(v)
print(c.weight)
print(c.noise)
print(c.vocalization)
print(c)
