from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,ename,eid):
        self.ename=ename
        self.eid=eid
        
        
    @abstractmethod
    def calculate_salary(self):
        pass
class FulltimeEmployee(Employee):
    def __init__(self,ename,eid,salary):
        super().__init__(ename,eid)
        self.salary=salary
        
    def calculate_salary(self):
        print("name:",self.ename)
        print("eid:",self.eid)
        print("salary:",self.salary)
class PartTimeEmployee(Employee):
    
    def __init__(self,ename,eid,hrs,perhr):
        super().__init__(ename,eid)
        self.hrs=hrs
        self.perhr=perhr
        
    def calculate_salary(self):
        
        print("name:",self.ename)
        print("eid:",self.eid)
        print(f"salary for {self.hrs}hrs is",self.hrs*self.perhr)

f=FulltimeEmployee("Vijay",102,120000)
f.calculate_salary()
p=PartTimeEmployee("Pavan",101,12,24)
p.calculate_salary()