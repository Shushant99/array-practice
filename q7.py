# rotate the array by k position to the right 
arr=[3,5,63,44,35,353,5,3,5,6,6,6,7,54,2,454,42,5,25,5000]
k=(int(input("enter no of postion ")))
newarr=arr[len(arr)-k:len(arr)][::-1]+arr[0:len(arr)-k]


print(newarr)

