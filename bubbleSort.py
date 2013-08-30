import random
import string

#datData = [1,3,25,18,54,2,77,16,18,19,20,32,10,43,33,46,100,165,1024,566,343,23,45]

def generateNums():

	f = open("numbers.txt", 'w')
	#nums = []
	for i in random.sample(range(500),500):
		print i
		f.write('%s,' % i)
	#print nums
	#return f
	f.close()

def readFromFile():
		with open("numbers.txt", 'r') as f:
			lines = []
			for x in f.readline():
				try: 
					lines.append(int(x))
					pass
				except ValueError, e:
					pass
				print lines

		return lines

def bubbleSort():
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
	return None

def main():
	generateNums()
	#isSorted = bubbleSort()
main()
