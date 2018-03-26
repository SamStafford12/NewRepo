class Dog:
   """ This is the beginning of a class for the dog"""

   def __init__(self,name):
       self.name = name

   def add_weight(self,weight):
       self.weight = weight

d = Dog("Furry")

x = Dog("Doggo")

x.add_weight(12)

print(d.name)
print(x.name)
print(x.weight)
