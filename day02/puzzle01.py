import copy

# checks decrease sequence
def checkDecrease(numbers):
	i = 0
	while i in range(len(numbers)):
		if (i == len(numbers) - 1):
			break

		if numbers[i] < numbers[i + 1] or numbers[i] - numbers[i + 1] > 3:
			return 0
		i += 1
	return 1

# check increase sequence
def checkIncrease(numbers):
	i = 0
	while i in range(len(numbers)):
		if (i == len(numbers) - 1):
			break

		if numbers[i] > numbers[i + 1] or numbers[i + 1] - numbers[i] > 3:
			return 0
		i += 1
	return 1

# check if sequence in initialy increasing or decreasing
def	isSafe(numbers):
	result = 0
	numbersValue = copy.deepcopy(numbers) # deep copy

	# check complete list
	if numbers[0] > numbers[1]:
		result = checkDecrease(numbers)
	elif numbers[0] < numbers[1]:
		result = checkIncrease(numbers)	

	if result == 1: 
		return True

	# check list removing one number at a time
	for i in range(len(numbers)):
		numbersValue.pop(i)
		if numbersValue[0] > numbersValue[1]:
			result = checkDecrease(numbersValue)
		elif numbersValue[0] < numbersValue[1]:
			result = checkIncrease(numbersValue)
		numbersValue = copy.deepcopy(numbers)
		if result == 1:
			return True

	return False

# get input from file
def getInput():
	contents = []
	while True:
		try:
			line = input()
		except EOFError:
			break
		contents.append(line)
	return contents

def myFunction():
	input1 = getInput()

	safe = 0
	for i in input1:
		control = 1
		numbers = i.split() # split input into list of numbers
		numbers =  [int(number) for number in numbers]
		safe += isSafe(numbers)
	
	print(safe)
		
myFunction()
