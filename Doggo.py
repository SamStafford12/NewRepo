class Dog:
   """ This is the beginning of a class for the dog"""

   def __init__(self,name):
       self.name = name

   def add_weight(self,weight):
       self.weight = weight

   def add_noise(self,noise):
      self.noise = noise

   def returnmethod(self):
      return "xyz"
      print("abc")


d = Dog("Furry")

x = Dog("Doggo")

s = x.returnmethod()
print(s)

x.add_weight(12)

x.add_noise("bark")


print(d.name)
print(x.name)
print(x.weight)
print(x.noise)

class Cat:

   def __init__(self,name):
      self.name = name

   def add_weight(self,weight):
       self.weight = weight

c = Cat("Furry")

z = Cat("Kat")

z.add_weight(8)


print(c.name)
print(z.name)
print(z.weight)


