

def fab(n):
    # a,b=0,0
    a,b=1,2
    list=[1,2]
    for i in range(2,n):
        list.append(list[i-2]+list[i-1])
    return list

l=fab(100)
print(l)


