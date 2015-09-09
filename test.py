# coding=utf-8


class Employee:

    "所有员工的基类"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def diplayEmployee(self):
        print "Name:", self.name, ", Salary: ", self.salary

emp1 = Employee("Zara", 2000)
emp2 = Employee("Mini", 5000)

emp1.diplayEmployee()
emp2.diplayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 7
emp1.age = 9

# delattr(emp1, 'age')
print getattr(emp1, 'age')

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
