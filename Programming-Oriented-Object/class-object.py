"""
les objets sont des instances de classes. Une classe est un plan (blueprint) pour créer des objets.
"""


class Person:

  # class attribute
  race = "human"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduction(self):
    return f"I'm {self.name} and I'm {self.age} years old"
  
  def birth_day(self):
    # increment the person's age
    self.age += 1
    return f"Happy birthday to me! Now I've got {self.age} years old"


if __name__ == "__main__":
  person_info = Person("salomon", 17)
  print(person_info.introduction())
  print(person_info.birth_day())