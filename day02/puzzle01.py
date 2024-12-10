import copy

# checks decrease sequence
def	checkDecrease(numbers):
	for i in range(len(numbers)):
		if i == len(numbers) - 1:
			break
		# if first number smaller than the second number or if difference between numbers greater than 3 return false
		if numbers[i] <= numbers[i + 1] or numbers[i] - numbers[i + 1] > 3:
			return False

	return True

# checks increase sequence
def	checkIncrease(numbers):
	for i in range(len(numbers)):
		if i == len(numbers) - 1:
			break
		# if first number greater than the second number or if difference between numbers greater than 3 return false
		if numbers[i] >= numbers[i + 1] or numbers[i + 1] - numbers[i] > 3:
			return False

	return True

# check if sequence in initialy increasing or decreasing
def	isSafe(numbers):
	if len(numbers) < 2:
		return True
	numbersValue = copy.deepcopy(numbers) # deep copy
	result = 0

	# check complete list
	if numbersValue[0] > numbersValue[1]:
		result = checkDecrease(numbersValue)
	elif numbersValue[0] < numbersValue[1]:
		result = checkIncrease(numbersValue)

	if result == 1: 
		return True

	# check list removing one number at a time
	for i in range(len(numbers) - 1):
		numbersValue.pop(i)
		if len(numbersValue) < 2:
			return True
		print(numbersValue)
		if numbersValue[0] > numbersValue[1]:
			result = checkDecrease(numbersValue)
		elif numbersValue[0] < numbersValue[1]:
			result = checkIncrease(numbersValue)
		if result == 1:
			return True
		numbersValue = copy.deepcopy(numbers)

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
		numbers = i.split() # split input into list of numbers
		numbers =  [int(number) for number in numbers]
		safe += isSafe(numbers)
	
	print(safe)
		
myFunction()
