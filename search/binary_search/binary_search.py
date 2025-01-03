# Implementation of binary search for the position of
# a specified value in an array of numbers. Binary search 
# takes a sorted array and iteratively splits the array 
# in half until the value is found. This code follows the 
# procedure described on the binary search Wikipedia page.

import math
import random
import numpy as np

# Example array
data = np.array((range(100)))
print(data)

# Determine the number of elements in the array
n = len(data)

# Specify a value to search for
T = 7

L = 0
R = n-1

while L <= R:
	m = math.floor((L+R)/2)  # Round down

	# Extract the m-th value in the array
	A_m = data[m]

	if A_m < T:
		L = m+1
	elif A_m > T:
		R = m-1
	else: 
		print("Found", T, "in position", m)
		break


