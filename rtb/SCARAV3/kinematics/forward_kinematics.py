import numpy as np
import math

""" Declaring our variables in mm unit"""

""" Parameters: a1 = 10, a2 = 10, a3 = 5, a4 = 10, d1 = 5, theta2 = 30 (Deg), theta3 = -45 (Deg)"""

# Link Lenghts

a1 = float(input("a1: "))
a2 = float(input("a2: "))
a3 = float(input("a3: "))
a4 = float(input("a4: "))

# Joint variables (prismatic = mm) (revolute = degrees)

d1 = float(input("d1: "))
theta2 = float(input("theta2: "))
theta3 = float(input("theta3: "))

# Degree to radian conversion using numpy

theta2 = np.deg2rad(theta2)
theta3 = np.deg2rad(theta3)

# For convenience
theta0 = np.deg2rad(0)

# Parametric table (DH-Table) (theta, alpha, r, d)

PT = [[theta0, theta0, 0, a1 + d1],
               [theta2, theta0, a2, 0],
               [theta3, theta0, a4, a3],]

# Homogenous TF Matrix Formula

""" Parametric table has 3 rows, so we will have 3 homogeous TF matrices """

H_list = []

for i in range(len(PT)):
    H = [[np.cos(PT[i][0]), -np.sin(PT[i][0]) * np.cos(PT[i][1]), np.sin(PT[i][0]) * np.sin(PT[i][1]), PT[i][2] * np.cos(PT[i][0])],
        [np.sin(PT[i][0]), np.cos(PT[i][0]) * np.cos(PT[i][1]), -np.cos(PT[i][0]) * np.sin(PT[i][1]), PT[i][2] * np.sin(PT[i][0])],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]]
    
    H_list.append(H)
    
# Printing the list of TF matrices

for i, H in enumerate(H_list):
    print(f'H{i}_{i+1} =\n', np.matrix(H))

""" Finding out the final result H0_3 (Moving from 0th frame to 3rd frame) """

# Step1: Finding H0_2 = H0_1 * H1_2

H0_2 = np.dot(H_list[0], H_list[1])

# Step2: Finding H0_3 = H0_2 * H2_3

H0_3 = np.dot(H0_2, H_list[2])

print(f'H0_3 =\n {np.around(H0_3, 3)}')


