#Write program that finds salaries greater than mean salary from dictionary.
# Import statistics Library
import numpy as np
name_to_salary_dictionary = {
    'Adam': 10000,
    'Beata': 12000,
    'Jarek': 7000,
    'Agnieszka': 8500,
    'Marek': 11200,
    'Ania': 9300,
    'Piotr': 15100,
    'Mateusz': 18000,
    'Agata': 16400,
    'Marian': 11000
}
mean_salary = np.mean(list(name_to_salary_dictionary.values()))
#print(str(mean_salary))

def get_salaries_above_mean():
    records_above_mean = []
    for name in name_to_salary_dictionary:
        record = {"name":name, "salary":name_to_salary_dictionary[name]}
        if record['salary']>mean_salary:
            records_above_mean.append(record)
    return records_above_mean

salaries_above_mean = get_salaries_above_mean()


print("Salaries greater than mean salary: "+str(mean_salary))
for record in salaries_above_mean:
    print("name: "+record['name']+" - salary: "+str(record['salary']))
    


