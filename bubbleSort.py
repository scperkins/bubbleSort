import random
import time
import string #not necessary but might use later

'''Generates a list with 50 indexes, populated with random numbers from 0 to 49 
and writes the list to a file called numbers.txt'''

def generateNums():
	global prompt
	prompt = input("Enter the size of your array as an integer: ")
	f = open("numbers.txt", 'w')
	for i in random.sample(range(prompt),prompt):
		f.write('%d,' % i)
	
	f.close()
	return prompt

'''Reads from numbers.txt, with correct formatting and converts back to integers, finally
appending the original random ints to a list. Returns the list 'lines'. '''

def readFromFile():
		with open("numbers.txt", 'r') as f:
			global lines
			lines = []
			for x in f.readline().split(','):
				try: 
					lines.append(int(x))
					pass
				except ValueError, e:
					pass

		print lines

		return lines

'''The bubble sort algorithm, takes the list from readFromFile as the only parameter, sorts it and Returns
the sorted list. '''

def bubbleSort(lines):
	global isSorted
	isSorted = True
	while isSorted:
		isSorted = False
		for i in range(len(lines)-1):
			if lines[i] >  lines[i+1]:
				#swap!
				lines[i], lines[i+1] = lines[i+1], lines[i]
				print lines
				isSorted = True
	return lines

'''Takes the sorted list as its parameter and writes it to a new file called bubbleSorted.txt '''
def writeFile(lines):
	f = open("bubbleSorted.txt", 'w')
	f.write('%s,' %lines)

def main():
	generateNums()
	readFromFile()
	startTime = time.time()
	isSorted = bubbleSort(lines)
	print " \nIt took", time.time()-startTime, "seconds to sort an array with", prompt, "indexes."
	writeFile(lines)
main()
