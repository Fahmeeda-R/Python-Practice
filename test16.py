class Student:
  def __init__(self,marks):
    self.__marks=marks
  def display(self):
    print("Marks:",self.__marks)
s1=Student(99)
s1.display()
