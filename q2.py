# Find the Maximum & Minimum Element

arr=[3,5,63,44,35,353,5,3,5,6,6,6,7,54,2,454,42,5,25,5000]
min=arr[0]
max=arr[0]
for i in range(len(arr)):
    if min>arr[i]:
        min=arr[i]
    elif arr[i]>max:
        max=arr[i]
print(min,max)
    