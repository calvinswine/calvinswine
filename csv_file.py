import csv
print()
count = 0
with open("vsc.csv", "r") as file1:
    data = csv.reader(file1, delimiter = ",")
    print("%20s"%"Emp No", "%20s"%"Emp Name", "%20s"%"Salary")
    print(" "*14 + "_"*48)
    for i in data:
        if int(i[2]) > 60000:
            print("%20s"%i[0], "%20s"%i[1], "%20s"%i[2])
print()