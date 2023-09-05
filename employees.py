class Employees:
    def __init__(self, id_num, name, salary) -> None:
        self.__id = id_num
        self.__name = name 
        self.__salary = salary
        
    def __str__(self) -> str:        
        return f"Employee ID: {self.__id}, Name: {self.__name}, Salary: {self.__salary}"
        
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def salary(self):
        return self.__salary
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary
    