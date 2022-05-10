n = int(input("N: "))
x = int(input("X: "))
group = list()
for i in range(1, (n*2)-(n-1)):
    group.append((i, ((n*2)-(i-1))))
print(group)
for i in group:
    if i[0] == x:
        print("Partner of chef:", i[1])
    elif i[1] == x:
        print("Partner of chef:", i[0])