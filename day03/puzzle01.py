import re

# get the result of multiplying both numbers
def	getProduct(list):
	return int(list[0]) * int(list[1])

# use regex to find all valid occurences of the mul(x,y) sequence
def getSequencesRegex(input1):
	pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)" # mul([0-999],[0-99]), do() and don't() regex pattern

	# find all occurrences of pattern in input and store it in a list
	regex = []
	for i in input1:
		for match in re.finditer(pattern, i):
			if match.group(1) and match.group(2):
				regex.append((match.group(1), match.group(2)))
			elif match.group(0):
				regex.append(match.group(0))

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

	sequences = getSequencesRegex(input1)

	# get the result of multiplying all sequences
	result = 0
	control = 0
	for i in sequences:
		if i == "don't()":
			control = 1
			continue
		elif i == "do()":
			control = 0
			continue
		if control == 1:
			continue
		result += getProduct(i)
	
	print(result)

myFunction()
