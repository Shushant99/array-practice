# remove given element from array
arr=[3,5,63,44,35,353,5,3,5,6,6,6,7,54,2,454,42,5,25,5000]
element=int(input("enter number you want to remove"))
if element in arr:
    arr.remove(element)
print(arr)

# removing all occurences
for i in arr:
    if i==element:
        arr.remove(i)
print(arr)