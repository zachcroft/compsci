# Implementation of a selection sorting algorithm for an array of integers

import random

# Generate random array of integers
data = list(range(1,100))
random.shuffle(data)

print("\nUnsorted array:\n")
print(data)

for i in range(0, len(data)):
	swap = False
	lowest = data[i]
	
	# Loop over the array and find the lowest value
	for x in range(i+1, len(data)):
		if data[x] < lowest:
			lowest   = data[x]
			position = x
			swap     = True

	# Place the lowest value in the correct spot
	if swap:
		temp = data[position]
		data[position] = data[i]
		data[i] = temp

	num_it += 1

print("\nSorted array:\n")
print(data)