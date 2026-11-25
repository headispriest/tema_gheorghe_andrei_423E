# Gheorghe Andrei
# => X = 6
# => Y = 8

class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {} # dict with task_name:status
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

## Typical status(es) for tasks in companies
##    New - just created
##    Pending / Asigned - manager asigned it to an employee
##    In progress - employee still working on it
##    Completed /Done - finished succesfully
##    Rejected - just created
##    Deprecated - no longer relevant
##    Blocked - hit a roadblock, can no longer work on it
        
##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
        
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0
    
    def __init__(self, name, salary, task, position, departament):
        super().__init__(name, salary)
        self.tasks = task
        self.position = position
        self.departament = departament
        Manager.mgr_count += 1

    def __del__(self):
        super().__del__()
        Manager.mgr_count -= 1

    # X = 6, X%6 = 0 => Afisez doar salariu
    def display_employee(self):
        print("Salary:", self.salary)

    def display_mgr_count(self):
        print(f"Total number of manager(s) is {Manager.mgr_count}")
    



emp1 = Employee("Alin","5000")

# Y = 8, Y/5 = 1, deci fac un singur obiect Manager
# X = 8, Y/5 = 1, deci ii atribui un singur task
# (Sper ca nu am inteles gresit cerinta)

mgr1 = Manager("Gigel", "10000", {"Eliminare Bottleneck":"In Progress"}, "Dev", "48_Gheorghe_Muntean")

emp1.display_emp_count()
mgr1.display_emp_count()

