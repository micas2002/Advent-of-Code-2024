# get words in diagonal position
def getWord(input1):
	count = 0
	rows = len(input1)
	col = len(input1[0])

	# left to right
	for v in range(1, rows - 1):
		for h in range(1, col - 1):
			if input1[v][h] == "A" and ((input1[v - 1][h - 1] == "M" and  input1[v + 1][h + 1] == "S") or \
				(input1[v - 1][h - 1] == "S" and  input1[v + 1][h + 1] == "M")):
				if (input1[v - 1][h + 1] == "M" and  input1[v + 1][h - 1] == "S") or \
					(input1[v - 1][h + 1] == "S" and  input1[v + 1][h - 1] == "M"):
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
	result += getWord(input1)

	print(result)


myFunction()
