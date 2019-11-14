

with open ("D:\\112.txt", "r") as myfile:
    data=myfile.readlines()
c = 0
index = []
long_data=[]
for i in range(len(data)):
    if c<=len(data[i]):
        c = len(data[i])
        long_data.append(data[i])
        index.append(i)
print(long_data)
print(index)

