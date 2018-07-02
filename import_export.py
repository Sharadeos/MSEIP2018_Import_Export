import csv
import random
import numpy as np


# numpy array
test_array = [[random.uniform(0, 255) for x in range(4096)] for y in range(10)]
np_test_array =  np.random.randint(low=0, high=255, size=(10,4096))

print("Generate and Save Array")
print(np_test_array[0])

# saving array
np.savetxt("foo.csv", np_test_array, delimiter=",")


# normal array
input = []
# numpy array
numpy_input = np.array([[]])


# reader array
with open('foo.csv', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	
	for row in csvreader:
		inputrow = []
		numpy_input_row = np.array([])
		for counter in range(len(row)):
			inputrow.append(int(float(row[counter])))
			numpy_input_row = np.append(numpy_input_row, float(row[counter]))
		#print(inputrow)
		input.append(inputrow)
		numpy_input = np.append(numpy_input, numpy_input_row)
		
		
print("Normal Array Loaded Values")
print(input[0])


numpy_input = np.asarray(numpy_input, dtype='int32')
numpy_input = np.reshape(numpy_input, (10, 4096))
print("Numpy Array Loaded Values")
print(numpy_input[0])
