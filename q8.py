# finding pair of sum that is equal to target (two sum) assuming pair always exist 
arr=[3,5,63,44,35,353,5,3,5,6,6,6,7,54,2,454,42,5,25,5000]
target=int(input("target"))
for i in range(len(arr)):
    for j in range(len(arr)):
        if i!=j:
            if arr[i]+arr[j]==target:
                print(arr[i],arr[j])