arr=[2,4,6,8,3]
n=len(arr)
c=arr[n-1]
print(c)
for i in range(n-2,-1,-1):
    if(arr[i] > c):
        arr[i+1] = arr[i]
        print(*arr,sep=" ")    
    else:
        arr[i+1] = c
        print(*arr,sep=" ")

target = arr[-1]
idx = n-2

while (target < arr[idx]) and (idx >= 0):
    arr[idx+1] = arr[idx]
    print(*arr)
    idx -= 1

arr[idx+1] = target
print(*arr)        