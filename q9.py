# removve duplicate dform arr without changing order
arr=[3,5,63,44,35,353,5,3,5,6,6,6,7,54,2,454,42,5,25,5000]
temparr=[]
for i in range(len(arr)):
    
    if arr[i] not in temparr:
        temparr.append(i)
        
    else:
       arr[i]=0
        
print(arr)
