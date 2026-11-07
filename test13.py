class Employee:
    def __init__ (self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
e1=Employee("Aisha",50000)
e2=Employee("Sara",30000)
e1.display()
e2.display()