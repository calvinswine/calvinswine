import csv
with open("vsc_write.csv", mode = 'w') as file1:
    data = csv.writer(file1, delimiter = ',')
    ans = 'y'
    while ans == 'y':
        eno = int(input("Enter the employee number: "))
        name = input("Enter the name of the employee: ")
        salary = int(input("Enter the salary of the employee: "))
        data.writerow([eno, name, salary])
        ans = input("Would you like to enter another employee data? (y/n) ")