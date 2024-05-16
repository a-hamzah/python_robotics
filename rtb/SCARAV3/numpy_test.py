import numpy as np

# Convert degrees to radians
degrees = 45
radians = np.deg2rad(degrees)

print("Degrees:", degrees)
print("Radians:", radians)

zero_mat = np.zeros((4, 4))
print(zero_mat)
print(zero_mat[1,:])
mat_size = zero_mat.shape
print(mat_size)

random_array = np.random.rand(4, 4)
arr_size = random_array.shape

print(arr_size[0])

PT = [[1, 3, 0, 7],
               [4, 0, 2, 0],
               [9, 5, 4, 3],]
print(PT)

def milimeters_to_meters(input):
    output = input/1000
    return output
    
    
value_in_meters = milimeters_to_meters(24)
print(value_in_meters)

