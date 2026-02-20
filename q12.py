# find the mising number in an array of size n contaning number from 1 to n
n=int(input("enter n: "))
arr=[range(1,n)]
arr.sort()
miss_nums=[]
for i in range(1,len(arr)):
    if i not in arr:
        miss_nums.append(i)
print(miss_nums)



# question not clear