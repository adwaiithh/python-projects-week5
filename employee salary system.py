class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Manager(Employee):
    def calculate_salary(self):
        bonus = 0.20 * self.base_salary  
        return self.base_salary + bonus


class Developer(Employee):
    def calculate_salary(self):
        bonus = 0.10 * self.base_salary   
        return self.base_salary + bonus


class Intern(Employee):
    def calculate_salary(self):
        stipend_deduction = 0.05 * self.base_salary   
        return self.base_salary - stipend_deduction


manager = Manager("Anjali", 80000)
developer = Developer("Rahul", 60000)
intern = Intern("Meera", 20000)

employees = [manager, developer, intern]

for emp in employees:
    print("Name:", emp.name)
    print("Base Salary:", emp.base_salary)
    print("Final Salary:", emp.calculate_salary())
    print("---------------------------")