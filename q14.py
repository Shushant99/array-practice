# find intersection of two array: find the common element between two array
arr1=[1,32,42,43,435,3,53,5,465,46,46,46,4,64,4]
arr2=[24,2,4,43,535,3,5,353,5,24,24,24,2,4,24,2]
common_elements=[]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] and arr2[j] in common_elements:
            pass
        else:
            if arr1[i]==arr2[j]:
                common_elements.append(arr1[i])

print(common_elements)