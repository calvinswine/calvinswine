# import csv
# with open("sport_csv_file.csv", mode = 'w') as file1:
#     data = csv.writer(file1, delimiter = ',')
#     again1 = True
#     while again1 == True:
#         competition = input("Enter the name of the competition: ")
#         sport = input("Enter the name of the sport: ")
#         team = input("Enter the name of the team which won the match: ")
#         prize = input("Enter the prize given to the winning team: ")
#         data.writerow([competition, sport, team, prize])
#         again2 = True
#         while again2 == True:
#             choice = input("Would you like to add more data? (y/n) ")
#             if choice == 'y':
#                 again2 = False
#             elif choice == 'n':
#                 again2 = False
#                 again1 = False
#             else:
#                 print("INVALID INPUT. CHOOSE AGAIN")

import csv
with open("sport_csv_file.csv", mode = 'r') as file1:
    data = csv.reader(file1, delimiter = ',')
    print("%20s"%"Competition", "%20s"%"Sport", "%20s"%"Team", "%20s"%"Prize")
    print("="*80)
    count = 0
    for i in data:
        print("%20s"%i[0], "%20s"%i[1], "%20s"%i[2], "%20s"%i[3])
        count += 1
    print("Total records:", count)