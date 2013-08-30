import random
import string

#datData = [1,3,25,18,54,2,77,16,18,19,20,32,10,43,33,46,100,165,1024,566,343,23,45]

def generateNums():

	f = open("numbers.txt", 'w')
	#nums = []
	for i in random.sample(range(50),50):
		#print i
		f.write('%d,' % i)
	#print nums
	#return f
	f.close()

def readFromFile():
		with open("numbers.txt", 'r') as f:
			global lines
			lines = []
			for x in f.readline().split(','):
				try: 
					lines.append(int(x))
					#print int(x)
					pass
				except ValueError, e:
					pass

		print lines

		return lines

def bubbleSort(lines):
	global isSorted
	isSorted = True
	while isSorted:
		isSorted = False
		for i in range(len(lines)-1):
			if lines[i] >  lines[i+1]:
				#swap!
				lines[i], lines[i+1] = lines[i+1], lines[i]
				#i=0
				print lines
				isSorted = True
	return lines

def writeFile(lines):
	f = open("bubbleSorted.txt", 'w')
	f.write('%s,' %lines)

def main():
	generateNums()
	readFromFile()
	isSorted = bubbleSort(lines)
	writeFile(lines)
main()
