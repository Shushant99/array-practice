# check if array is shorted
arr=[3,5,63,44,35,353,5,3,5,6,6,6,7,54,2,454,42,5,25,5000]
# arr=[2,3,5,7,8,9,12,34,56,78,90,134,345]
shorted_arr=sorted(arr)
if arr==shorted_arr:
    print("shorted")
else:
    print("not shorted")