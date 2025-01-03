# Implementation of a bubble sorting algorithm for an array of integers

data = [6, 3, 9, 7, 1, 2, 5, 4, 8]

num_it = 0     # number of iterations
sorted = False

while sorted == False:
	sorted = True

	for x in range(len(data) - 1):
		# If an entry is larger than its neighbor 
		# on the right then swap them
		if data[x+1] < data[x]:
			temp      = data[x]
			data[x]   = data[x+1]
			data[x+1] = temp
			sorted = False
		else:
			continue

	num_it += 1

print("Array was sorted in ", num_it, " iterations.")
print(data)