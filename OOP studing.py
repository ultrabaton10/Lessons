#  команда dir() показывает список всех методов и свойств объекта
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

try:
    print(p1.age)  # Здесь вылетает ошибка AttributeError,
                   # потому что экземпляр класса Person p1 больше не имеет свойства age,
                   # так как мы его удалили
except AttributeError:
    p2 = Person('I', 173)
    print(p2.age)
