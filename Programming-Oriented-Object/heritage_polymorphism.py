"""
les heritages en python
"""


class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    raise NotImplementedError("method not implemented")
  
  def description(self):
    return f"{self.name} is {self.age} years old"
  
class Dog(Animal):
  def speak(self):
    return "Woof!"
  
  def hunter(self):
    return f"{self.name} goes hunting"
  
class Cat(Animal):
  def speak(self):
    return "Meow!"

  def climb(self):
    return f"{self.name} climbs a tree"
def main():
  Dog = Dog("Almand", 5)
  Cat = Cat("Miauuu!", 2)

  animals = [Dog, Cat]
  for animal in animals:
    print(f"{animal.description()} - {animal.speak()}")


if __name__ == "__main__":
  main()