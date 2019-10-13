for _ in range(int(input())):
    s=input()
    k=int(input())
    l=len(s)
    i=0
    f=[]
    while i<len(s):
        f.append(s[i:i+k])
        i+=k
    print(f)