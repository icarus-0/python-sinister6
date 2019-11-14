# Reding n lines from a Text file

n = int(input("enter the number of lines"))

f = open("D:\\112.txt",'r')

for i in range(n):
    print(f.readline())
f.close()