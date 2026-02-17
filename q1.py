arr=[1,4,5,7,8,9,9,10,11,12,13,14,15,16,17,18,19,20]
rev_arr=[]
for i in range(len(arr)):
    rev_arr.append(arr[len(arr)-1-i])
print(rev_arr)

rev_arr2=arr[::-1]
print(rev_arr2)

