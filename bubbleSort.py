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

def bubbleSort():
	global isSorted
	isSorted = True
	while isSorted:
		isSorted = False
		with open("numbers.txt", 'r') as f:
			li = map(int, string.split(f.readline()))
			print li
			'''
			for i in range(len(lines)-1):
				if lines[i] >  lines[i+1]:
					#swap!
					lines[i], lines[i+1] = lines[i+1], lines[i]
					#i=0
					print lines
					isSorted = True
	return None
'''
def main():
	generateNums()
	isSorted = bubbleSort()
main()