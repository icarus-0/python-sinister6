# Append text in a pre exiting Text file

f = open("D:\\112.txt",'a')
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()