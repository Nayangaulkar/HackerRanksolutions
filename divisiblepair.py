n=6
ar=[1,3,2,6,1,2]
k=3
count=0
for i in range(0,n):
    for j in range(i+1,n):
        sum = ar[i]+ar[j]
        if( i<j and sum % k== 0 ):
            count+=1
        sum=0
print(count)          