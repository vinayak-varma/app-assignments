class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def categorize(self):
        if self.salary>=70000:
            return "High Salary"
        elif self.salary>=40000:
            return "Medium Salary"
        else:
            return "Low Salary"
    def display(self):
        print(f"{self.emp_id}\t{self.name}\t\t{self.salary}\t\t{self.categorize()}")
class Company:
    def __init__(self,name):
        self.company_name=name
        self.employee_list=[]
    def add_employee(self,emp_id,name,salary):
        emp = Employee(emp_id,name,salary)
        self.employee_list.append(emp)
        print(f"Employee '{name}' added successfully!\n")
    def display_all_employees(self):
        print("-" * 55)
        print("ID\tName\t\tSalary\t\tCategory")
        print("-" * 55)
        for emp in self.employee_list:
            emp.display()
        print("-" * 55)
company = Company("ABC Technologies")
while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        emp_id=input("Enter Employee ID: ")
        name=input("Enter Employee Name: ")
        salary=float(input("Enter Employee Salary: "))
        company.add_employee(emp_id, name, salary)
    elif choice==2:
        company.display_all_employees()
    elif choice==3:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")