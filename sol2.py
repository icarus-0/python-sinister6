def fund(l,k):
    x=[]
    for i in range(len(l)):
        su=0

        for j in range(i,len(l)):
            su+=l[j]
            if su<=k:
                x.append(l[j])
            else:
                break
        if sum(x)==k:
            break
        else:
            x=[]
    if len(x)>0:
        return x
    else:
        return None


l=eval(input())
k=int(input())
print(fund(l,k))