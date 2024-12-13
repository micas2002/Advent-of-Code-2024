# get words in diagonal position
def getDiagonal(input1):
	count = 0
	rows = len(input1)
	col = len(input1[0])

	# left to right
	for v in range(rows - 3):
		for h in range(col - 3):
			if (input1[v][h] == "X" and input1[v + 1][h + 1] == "M" and  input1[v + 2][h + 2] == "A" and input1[v + 3][h + 3] == "S") or \
			(input1[v][h] == "S" and input1[v + 1][h + 1] == "A" and  input1[v + 2][h + 2] == "M" and input1[v + 3][h + 3] == "X"):
				count += 1

	# right to left
	for v in range(rows - 3):
		for h in range(3, col):
			if (input1[v][h] == "X" and input1[v + 1][h - 1] == "M" and input1[v + 2][h - 2] == "A" and input1[v + 3][h - 3] == "S") or \
			(input1[v][h] == "S" and input1[v + 1][h - 1] == "A" and input1[v + 2][h - 2] == "M" and input1[v + 3][h - 3] == "X"):
				count += 1

	return count

# get words in vertical position
def	getVertical(input1):
	count = 0
	for h in range(len(input1[0])):
		for v in range(len(input1)):
			if len(input1) - v < 4:
				break
			if (input1[v][h] == "X" and input1[v + 1][h] == "M" and input1[v + 2][h] == "A" and input1[v + 3][h] == "S") or \
				(input1[v][h] == "S" and input1[v + 1][h] == "A" and input1[v + 2][h] == "M" and input1[v + 3][h] == "X"):
					count += 1
					v += 3
	return count

# get words in horizontal position
def	getHorizontal(input1):
	count = 0
	for v in range(len(input1)):
		for h in range(len(input1[v])):
			if input1[v][h:h + 4] == "XMAS" or input1[v][h:h + 4] == "SAMX":
					count += 1
	return count

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

	result = 0
	result += getHorizontal(input1)
	result += getVertical(input1)
	result += getDiagonal(input1)

	print(result)


myFunction()
