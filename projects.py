class Projects:
    def __init__(self, name, initial_date, end_date, elapsed_time, employee) -> None:
        self.__name = name
        self.initial_date = initial_date
        self.end_date = end_date
        self.elapsed_time = elapsed_time
        self.employee_inCharge = employee
        
    @property
    def name(self):
        return self.__name
    @property
    def initial_date(self):
        return self.initial_date
    @property
    def end_date(self):
        return self.end_date
    @property
    def elapsed_time(self):
        return self.elapsed_time
    @property
    def employee_inCharge(self):
        return self.employee_inCharge.id
    
    @initial_date.setter
    def initial_date(self,new_initDate):
        self.initial_date = new_initDate
    @end_date.setter
    def end_date(self,new_endDate):
        self.end_date = new_endDate
    @elapsed_time.setter
    def initial_date(self,new_elapsedTime):
        self.elapsed_time = new_elapsedTime
    @employee_inCharge.setter
    def employee_inCharge(self, new_employee):
        self.employee_inCharge = new_employee
        
    