class Employee:
    def __init__(self,name,salary):
        self.salary=salary
        self.name=name
        
    def display_details(self):
        print(self.name,"name of the employee")
        print(self.salary ,"is the salary of the employee")
        
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size
        
    def display_role(self):
       
        print(f"{self.name:^5}THE MANAGER")
        print("teamSIze:", self.team_size)
class Engineer(Employee):
    def __init__(self,name,salary,specification):
        super().__init__(name,salary)
        self.specification=specification
        
    def display_role(self):
        
        print(f"{self.name:^5}  THE Engineer")
        print("specification:", self.specification)

m1=Manager("VIJAY",100000,10)
m1.display_details()
m1.display_role()
print("="*32)
e1=Engineer("PAVAN",100000,"AIML")
e1.display_details()
e1.display_role()

        