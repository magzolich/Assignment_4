# Write program that reads csv file and calculates compensation as: (employment_duration_in_years * 1000 zł) 
# only when employment_duration_in_years is greater or equal 5

import csv 

def print_compensation(employess_data_list):
    # print()
    #employees_compensation_eligible = []
    for employee in employess_data_list:
        if int(employee['Duration of employment in years'])>=5:
            compensation = int(employee['Salary'])*1000
            print('name: '+ employee['Name']+' - compensation: '+str(compensation))
            # name: Beata - compensation: 5000
            # record = {"name: " : employee['Name'], "compensation: " : str(compensation)}
            # employees_compensation_eligible.append(record) 
    #return employees_compensation_eligible
   

file = open('5_input.csv','r')
reader = csv.DictReader(file)
employees_data_list = list(reader)
print(employees_data_list)
print_compensation(employees_data_list)
