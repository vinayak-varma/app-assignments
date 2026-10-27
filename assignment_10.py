import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("Original Array:", arr)
print("First three numbers:", arr[:3])
print("Numbers 3 to 7:", arr[3:8])
print("Reversed array:", arr[::-1])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
broadcast_arr = (arr+10)
print("Array after broadcasting:", broadcast_arr)
