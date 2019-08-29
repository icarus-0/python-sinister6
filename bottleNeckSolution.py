n = int(input("enter the number of bottles"))

radius = list(map(int,input().split(" ")))
filled = []

for i in radius:
    filled.append(radius.count(i))


print(max(filled))
