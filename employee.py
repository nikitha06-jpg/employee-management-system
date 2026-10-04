# employee.py
# Contains the Employee parent class and its child classes.


class Employee:
    """Parent class: holds the details every employee has."""

    def __init__(self, emp_id, name, department, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def display(self):
        print(f"{self.emp_id} | {self.name} | Employee | {self.department} | "
              f"Salary: {self.calculate_salary()}")

    def to_dict(self):
        return {
            "type": "employee",
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "base_salary": self.base_salary,
        }


class Developer(Employee):
    """Child class: a developer earns a bonus for every project completed."""

    def __init__(self, emp_id, name, department, base_salary, projects_completed):
        super().__init__(emp_id, name, department, base_salary)
        self.projects_completed = projects_completed

    def calculate_salary(self):
        return self.base_salary + (self.projects_completed * 2000)

    def display(self):
        print(f"{self.emp_id} | {self.name} | Developer | {self.department} | "
              f"Projects: {self.projects_completed} | Salary: {self.calculate_salary()}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "developer"
        data["projects_completed"] = self.projects_completed
        return data


class Manager(Employee):
    """Child class: a manager earns a bonus for every team member."""

    def __init__(self, emp_id, name, department, base_salary, team_size):
        super().__init__(emp_id, name, department, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        return self.base_salary + (self.team_size * 1500)

    def display(self):
        print(f"{self.emp_id} | {self.name} | Manager | {self.department} | "
              f"Team Size: {self.team_size} | Salary: {self.calculate_salary()}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "manager"
        data["team_size"] = self.team_size
        return data
