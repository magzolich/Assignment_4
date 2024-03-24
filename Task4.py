#Write program that maps employee id to first letter of name, technically means returns a dictionary, where:
#-  key - an employee's id,
#-  value - first letter of name

employees = [
{'Id': 1, 'Name': 'Adam', 'Department': 'Management', 'Salary': 10000},
{'Id': 2, 'Name': 'Beata', 'Department': 'Management', 'Salary': 12000},
{'Id': 3, 'Name': 'Jarek', 'Department': 'Kitchen', 'Salary': 7000},
{'Id': 4, 'Name': 'Agnieszka', 'Department': 'House Floor', 'Salary': 8500},
{'Id': 5, 'Name': 'Marek', 'Department': 'House Floor', 'Salary': 11200},
{'Id': 6, 'Name': 'Ania', 'Department': 'Kitchen', 'Salary': 9300},
{'Id': 7, 'Name': 'Piotr', 'Department': 'Management', 'Salary': 15100},
{'Id': 8, 'Name': 'Mateusz', 'Department': 'Cashier', 'Salary': 18000},
{'Id': 9, 'Name': 'Agata', 'Department': 'Management', 'Salary': 16400},
{'Id': 10, 'Name': 'Marian', 'Department': 'Cashier', 'Salary': 11000},
]


def get_employees_letter_ids():
    letter_and_id = []
    for employee in employees: 
        record = {employee['Id']:employee['Name'][0]}
        letter_and_id.append(record)
    return letter_and_id

employees_letter_ids = get_employees_letter_ids()
print(employees_letter_ids)