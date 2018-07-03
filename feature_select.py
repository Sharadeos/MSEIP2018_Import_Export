import csv
import random
import numpy as np

imageCount = 1
imageSize = 16


# numpy array
test_array = [[random.uniform(0, 255) for x in range(imageSize*imageSize)] for y in range(imageCount)]
np_test_array =  np.random.randint(low=0, high=255, size=(imageCount,imageSize*imageSize))

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
#print(input[0])


numpy_input = np.asarray(numpy_input, dtype='int32')
numpy_input = np.reshape(numpy_input, (imageCount, imageSize*imageSize))
print("Numpy Array Loaded Values")
print(numpy_input)


print("Feature Selection")
# Feature Selection
# 64 x 64 greyscale image

imageCount = 1
imageSize = 16
columnSize = imageSize

columnAccumulator = []#[[0 for x in range(imageSize*imageSize)] for y in range(imageCount)] 


columnDerivatives = [0 for x in range(columnSize)]

for columnCounter in range(columnSize):
	
	columnAccumulator = []
	for imageCounter in range(imageCount):
		
		
		for columnMover in range(imageSize):
		
			columnAccumulator.append(numpy_input[imageCounter][(imageSize*columnMover)+columnCounter])
	print(columnAccumulator)

	
	columnDerivatives[columnCounter] = np.std(columnAccumulator)
	print("Standard Deviation for Column:", columnCounter, "is", columnDerivatives[columnCounter])