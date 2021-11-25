#10 2 3
#3 1
#5 2 8 
b=[10,2,3]                         
keyboards=[3,1]
drives=[5,2,8]
tsum=[-1]
budget = max(b)
for i in range(len(keyboards)):
    for j in range(len(drives)):
        sum=keyboards[i]+drives[j]
        if(sum<budget):
            tsum.append(sum)



if(max(tsum) < budget):
    print(max(tsum))
else:
    print(-1)



#max =tsum[0]
#for i in range(len(tsum)):
 #   if(tsum[i]>max):
  #      max=tsum[i]
#if(max<budget):
 #   print(max)
#else:
#    print(-1)


