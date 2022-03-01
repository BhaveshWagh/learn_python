# Example using elif as well
# Print the meteorological season for each month (loosely, of course, and in the Northern Hemisphere)
print("In the Northern Hemisphere: \n")
month_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # i.e., January is 1, February is 2, etc...
for month in month_integer:
    if month < 3:
        print("Month {} is in Winter".format(month))
    elif month < 6:
        print("Month {} is in Spring".format(month))
    elif month < 9:
        print("Month {} is in Summer".format(month))
    elif month < 12:
        print("Month {} is in Fall".format(month))
    else: # This will put 12 (i.e., December) into Winter
        print("Month {} is in Winter".format(month))

print("--" * 80)
import numpy as np

x = np.array([2, 4, 6]) # create a rank 1 array
A = np.array([[1, 3, 5], [2, 4, 6]]) # create a rank 2 array
B = np.array([[1, 2, 3], [4, 5, 6]])

print("Matrix A: \n")
print(A)

print("\nMatrix B: \n")
print(B)
