# Find the Second Largest Element
arr=[3,5,63,44,35,353,5,3,5,6,6,6,7,54,2,454,42,5,25,5000]
sec_larg=0
large=0
for i in range(len(arr)):
    if arr[i]>large:
        sec_larg=large
        large=arr[i]
print(sec_larg)
        