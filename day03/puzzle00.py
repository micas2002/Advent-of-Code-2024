import re

# get the result of multiplying both numbers
def	getProduct(list):
	return int(list[0]) * int(list[1])

# use regex to find all valid occurences of the mul(x,y) sequence
def	getSequencesRegex(input1):
	pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)' # mul([0-999],[0-99]) regex pattern

	# find all occurrences of pattern in input and store it in a list
	regex = []
	for i in input1:
		regex += re.findall(pattern, i)

	return regex
	
# Get input from file or console
def getInput():
	contents = []
	while True:
		try:
			line = input()
		except EOFError:
			break
		contents.append(line.strip())
	return contents

# Main function to process input and count safe sequences
def myFunction():
	input1 = getInput()

	# get sequences
	sequences = getSequencesRegex(input1)

	# get the result of multiplying all sequences
	result = 0
	for i in sequences:
		result += getProduct(i)
	
	print(result)

myFunction()
