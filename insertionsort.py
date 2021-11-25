
arr = [2,1,3,1,2]
count=0
for i in range(1,len(arr)):
    j=0
    while(j<i):
        if(arr[j] >arr[i]):
            count+=1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        j+=1
    print(arr)
print(count)        
    
  

      

