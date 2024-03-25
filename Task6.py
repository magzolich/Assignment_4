# 6.* LEVEL_3_hard Write program the same program as in 5. but having date of employment instead of employment_duration_in_years.

import csv
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


def print_compensation(employess_data_list):
    today = date.today()
    for employee in employess_data_list:
        employment_datetime = datetime.strptime(
            employee["Date of employment"], "%Y-%m-%d")
        employment_date = employment_datetime.date()
        difference_in_years = relativedelta(today, employment_date).years

        if difference_in_years >= 5:
            compensation = int(employee['Salary'])*1000
            print('name: ' + employee['Name'] +
                  ' - compensation: '+str(compensation))


def main():
    file = open('6_input.csv', 'r')
    reader = csv.DictReader(file)
    employees_data_list = list(reader)
    print(employees_data_list)
    print_compensation(employees_data_list)


if __name__ == "__main__":
    main()
