#Write program that finds max 3 salaries from the list.
salaries = [10000, 12000, 7000, 8500, 11200, 9300, 15100, 18000, 16400, 11000]
salaries.sort(reverse=True)
print("Top salaries in the provided range are: " + str(salaries[0:3]))
