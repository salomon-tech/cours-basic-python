class Peaple:

  #class atribute
  race = "nigga"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduction(self):
    return f"i'm {self.name} and i've {self.age} years old"
  
  def birth_day(self):
    self.birth_day += 1
    return f"happy birthday to me! now i've got {self.age} years old"
  
  person_info = Peaple("salomon", 17)
  print(person_info.introduction())
  print(person_info.birth_day())