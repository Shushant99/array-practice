# count frequency of number
arr=[3,5,63,44,35,353,2,5,3,5,6,6,6,7,54,2,454,42,5,25,5000,5000]
freq={}

for i in arr:
    count=0
    key=i
    for i in arr:
        if key==i:
            count+=1
    
    freq.update({f"{key}":count})
        
print(freq)