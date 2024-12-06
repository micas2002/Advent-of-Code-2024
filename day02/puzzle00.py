# checks decrease sequence
def checkDecrease(numbers):
	for i in range(len(numbers)):
		if (i == len(numbers) - 1):
			break
		# check if first numbers is lesses than the second and checks if the second number is in the correct range
		if numbers[i] < numbers[i + 1] or numbers[i + 1] not in range(numbers[i] - 3, numbers[i]):
			return 0
	return 1

# check increase sequence
def checkIncrease(numbers):
	for i in range(len(numbers)):
		if (i == len(numbers) - 1):
			break
		# check if first numbers is greater than the second and checks if the second number is in the correct range
		if numbers[i] > numbers[i + 1] or numbers[i + 1] not in range(numbers[i] + 1, numbers[i] + 4):
			return 0
	return 1

# check if sequence in initialy increasing or decreasing
def	isSafe(line):
	numbers = line.split()
	numbers =  [int(number) for number in numbers]

	if numbers[0] > numbers[1]:
		return checkDecrease(numbers)
	elif numbers[0] < numbers[1]:
		return checkIncrease(numbers)
	else:
		return 0

# get input from user
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
		safe += isSafe(i)
	
	print(safe)
		
myFunction()
