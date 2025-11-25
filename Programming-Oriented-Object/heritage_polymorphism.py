class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    raise NotImplementedError("methode not implemented")
  
  def description(self):
    return f"{self.name} have {self.age} years old"
  
class Dog:
  def speak(Animal):
    return "wooof!!!"
  
  def hunter(self):
    return f"{self.name} go to hunt"
  
class Cat(Animal):
  def climb(self):
    return f"{self.name} climb a tree"
  
B = Cat("Miauuu!", 2)
A = Dog("Almand", 5)

animals = [Dog, Cat]
for animal in animals:
  print(f"{animal.description()} - {animal.speak()}")