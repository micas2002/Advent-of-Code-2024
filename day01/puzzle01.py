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

	# remove white spaces
	for i in range(len(input1)):
		input1[i] = input1[i].split("   ")

	list1 = []
	list2 = []
	
	# create a separate list for each list
	for i in range(len(input1)):
		list1.append(input1[i][0])
		list2.append(input1[i][1])
	
	# sort both lists
	list1.sort()
	list2.sort()

	# calculate similarity score by adding up each number in the list1
	# after multiplying it by the number of times that number appears in the list2
	result = 0
	for i in range(len(list1)):
		result += list2.count(list1[i]) * int(list1[i])

	print(result)

myFunction()
