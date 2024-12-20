def	isValid(rules, sequence, pos):
	# get first instance of rule to check
	i = 0
	while i in range(len(rules)) and rules[i][0] != sequence[pos]:
		i += 1

	if i == len(rules) - 1:
		return 1

	# loop over sequence to check if its valid
	x = i
	while i in range(len(rules)) and rules[i][0] == rules[x][0]:
		# if page of rule exists return index, else skip
		index_value = sequence.index(rules[i][1]) if rules[i][1] in sequence else -1
		print(index_value)
		if index_value == -1: # skip if page does not exist
			i += 1
			continue
		if index_value < i: # return 0 if not up to the rules
			return 0
		i += 1
	
	return 1
		

def	checkSequence(rules, sequence):
	# check each member of sequence
	for i in range(1, len(sequence)):
		value = isValid(rules, sequence, i)
		if value == 0:
			return 0
	
	return 1

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

	rules = []
	sequences = []
	appendSequences = False
	for i in input1:
		if i == "":
			appendSequences = True
			continue
		if appendSequences == False:
			rules.append(i.split('|'))
		else:
			sequences.append(i.split(','))
	
	rules.sort()
	print(rules	)
	print(checkSequence(rules, sequences[0]))

myFunction()
