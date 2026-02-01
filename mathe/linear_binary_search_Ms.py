#Linear Search
def linear_search(data,target):
    for index, element in enumerate(data):       
        if element==target:
            return index
    return -1
        

unsorted_data = [5, 12, 2, 91, 16, 23, 8, 38, 72, 56]
target_value = 19
 
print("Linear search")
index = linear_search(unsorted_data,target_value)
if index!=-1:
    print(f"Der Index von {target_value} ist {index}")
else:
    print(f"Die Zahl {target_value} ist nicht in der Liste")

print("-"*30)

#Binary search
def binary_search(data,target):
    low=0
    high = len(data)-1
    while low<=high:
        mitte = (low+high)//2
        if data[mitte]< target:
            low = mitte+1
        elif data[mitte]> target:
            high = mitte-1
        else:
            return mitte
    return -1
        # if high-low==1:
        #         if target==data[low]:
        #             return low
        #         elif target==data[high]:
        #             return high
        #         else: return -1
 
number=[2,5,8,12,16,23,38,56,72,91]
target_value=120

print("Binary search") 
index = binary_search(number,target_value)
if index!=-1:
    print(f"Der Index von {target_value} ist {index}")
else:
    print(f"Die Zahl {target_value} ist nicht in der Liste")