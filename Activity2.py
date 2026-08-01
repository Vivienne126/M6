def minelement(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=min(temp,a[i])
    return temp

def maxelement(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=max(temp,a[i])
    return temp


a=[-12,234,456,762,12345,43213,1,2]
size=len(a)

print(f"Minimum element is : {minelement(a,size)}")
print(f"Maximum element is: {maxelement(a,size)}")