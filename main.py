# main.py
# The menu program. It imports the classes from employee.py.

import json
from employee import Employee, Developer, Manager

FILE_NAME = "employees.json"
employees = []          # this list will hold all the employee objects


def get_number(prompt):
    """Keep asking until the user types a valid whole number.
    This one is done for you. Use it every time you need a number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")


def find_employee(emp_id):
    """Return the employee with this ID, or None if there isn't one."""
    for employee in employees:
        if employee.emp_id == emp_id:
            return employee

    return None


def add_employee():
    employee_type = input("Enter employee type (developer/manager): ").strip().lower()

    if employee_type not in ["developer", "manager"]:
        print("Invalid employee type.")
        return

    emp_id = get_number("Enter employee ID: ")

    if find_employee(emp_id):
        print("Employee ID already exists.")
        return

    name = input("Enter name: ")
    department = input("Enter department: ")
    base_salary = get_number("Enter base salary: ")

    if employee_type == "developer":
        projects_completed = get_number("Enter projects completed: ")

        employee = Developer(
            emp_id,
            name,
            department,
            base_salary,
            projects_completed
        )

    else:
        team_size = get_number("Enter team size: ")

        employee = Manager(
            emp_id,
            name,
            department,
            base_salary,
            team_size
        )

    employees.append(employee)

    print("Employee added successfully.")


def view_employees():
    if not employees:
        print("No employees yet.")
        return

    for employee in employees:
        employee.display()


def search_employee():
    emp_id = get_number("Enter employee ID: ")
    employee = find_employee(emp_id)

    if employee:
        employee.display()
    else:
        print("Not found.")


def delete_employee():
    emp_id = get_number("Enter employee ID: ")
    employee = find_employee(emp_id)

    if employee:
        employees.remove(employee)
        print("Employee deleted.")
    else:
        print("Not found.")


def save_to_file():
    data = []

    for employee in employees:
        data.append(employee.to_dict())

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Employees saved successfully.")


def load_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No saved employee file found.")
        return

    employees.clear()

    for item in data:
        if item["type"] == "developer":
            employee = Developer(
                item["emp_id"],
                item["name"],
                item["department"],
                item["base_salary"],
                item["projects_completed"]
            )
        else:
            employee = Manager(
                item["emp_id"],
                item["name"],
                item["department"],
                item["base_salary"],
                item["team_size"]
            )

        employees.append(employee)

    print("Employees loaded successfully.")


# ---------------------------------------------------------------
# The menu loop is done for you. You do not need to change it.
# ---------------------------------------------------------------
def main():
    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
