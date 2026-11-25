import employee as emp

def test_emp1_init():
    "Test pentru initializarea corecta a lui emp1"
    assert emp.emp1.name == "Alin"
    assert emp.emp1.salary == "5000"

def test_emp1_update_salary():
    "Test pentru update_salary(new_salary)"
    emp.emp1.update_salary("6000")
    assert emp.emp1.salary == "6000"

def test_emp1_modify_task():
    "Testare pentru atribuire de task cu status implicit (New), atribuire cu alt status, si modificare"
    emp.emp1.modify_task("Depanare")
    emp.emp1.modify_task("Rescriere", "Pending")
    assert emp.emp1.tasks["Depanare"] == "New"
    assert emp.emp1.tasks["Rescriere"] == "Pending"
    emp.emp1.modify_task("Depanare", "Deprecated")
    assert emp.emp1.tasks["Depanare"] == "Deprecated"

def test_mgr1_init():
    "Test pentru initializarea lui mgr1"
    assert emp.mgr1.name == "Gigel"
    assert emp.mgr1.salary == "10000"
    assert emp.mgr1.tasks["Eliminare Bottleneck"] == "In Progress"
    assert emp.mgr1.position == "Dev"
    assert emp.mgr1.departament == "48_Gheorghe_Muntean"

def test_mgr1_update_salary():
    "Test pentru update_salary(new_salary)"
    emp.mgr1.update_salary("12000")
    assert emp.mgr1.salary == "12000"

def test_emp1_modify_task():
    "Testare pentru atribuire de task cu status implicit (New), atribuire cu alt status, si modificare"
    emp.mgr1.modify_task("Depanare")
    emp.mgr1.modify_task("Rescriere", "Pending")
    assert emp.mgr1.tasks["Depanare"] == "New"
    assert emp.mgr1.tasks["Rescriere"] == "Pending"
    emp.mgr1.modify_task("Depanare", "Deprecated")
    assert emp.mgr1.tasks["Depanare"] == "Deprecated"

def test_Employee_empCount():
    "Test pentru functionarea corecta a empCount"
    assert emp.Employee.empCount == 2
    emp2 = emp.Employee("Marcel", "2000")
    mgr2 = emp.Manager("Vasile", "8000", {"Depanare":"New"}, "QA", "48_Gheorghe_Muntean")
    assert emp.Employee.empCount == 4
    del emp2
    assert emp.Employee.empCount == 3
    del mgr2
    assert emp.Manager.empCount == 2

def test_Manager_empCount():
    assert emp.Manager.empCount == 2
    emp2 = emp.Employee("Marcel", "2000")
    mgr2 = emp.Manager("Vasile", "8000", {"Depanare":"New"}, "QA", "48_Gheorghe_Muntean")
    assert emp.Manager.empCount == 4
    del emp2
    assert emp.Manager.empCount == 3
    del mgr2
    assert emp.Manager.empCount == 2

def test_Manager_mgr_count():
    assert emp.Manager.mgr_count == 1
    mgr2 = emp.Manager("Vasile", "8000", {"Depanare":"New"}, "QA", "48_Gheorghe_Muntean")
    assert emp.Manager.mgr_count == 2
    del mgr2
    assert emp.Manager.mgr_count == 1

