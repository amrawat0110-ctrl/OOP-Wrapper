class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name="", age=0, employee_id="", salary=0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter
    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    # Setter
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $", self.__salary)

    def __del__(self):
        print("Employee object deleted.")


class Manager(Employee):
    def __init__(self, name="", age=0, employee_id="", salary=0, department=""):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name="", age=0, employee_id="", salary=0, language=""):
        super().__init__(name, age, employee_id, salary)
        self.language = language

    def display(self):
        print("\nDeveloper Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Programming Language:", self.language)


print("Is Manager subclass of Employee?", issubclass(Manager, Employee))
print("Is Developer subclass of Employee?", issubclass(Developer, Employee))

person = None
employee = None
manager = None
developer = None

while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Create Developer")
    print("5. Show Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        person = Person(name, age)
        print("\nPerson created successfully.")

    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        employee = Employee(name, age, emp_id, salary)
        print("\nEmployee created successfully.")

    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        manager = Manager(name, age, emp_id, salary, dept)
        print("\nManager created successfully.")

    elif choice == 4:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        lang = input("Enter Programming Language: ")
        developer = Developer(name, age, emp_id, salary, lang)
        print("\nDeveloper created successfully.")

    elif choice == 5:
        print("\n1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")
        sub = int(input("Enter choice: "))

        if sub == 1 and person:
            person.display()
        elif sub == 2 and employee:
            employee.display()
        elif sub == 3 and manager:
            manager.display()
        elif sub == 4 and developer:
            developer.display()
        else:
            print("Data not available.")

    elif choice == 6:
        print("\nExiting the system. All resources have been freed.")
        break

    else:
        print("Invalid choice!")

print("Goodbye!")


