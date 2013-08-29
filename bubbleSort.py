import random

datData = [1,3,25,18,54,2,77,16,18,19,20,32,10,43,33,46,100,165,1024,566,343,23,45]

def generateNums():
	#f = open("numbers.txt", 'w')
	nums = []
	for i in range(10000):
		nums = random.sample(xrange(1000),1000)
	print nums

def bubbleSort(datData):
	global isSorted
	isSorted = False
	for i in range(len(datData)-1):
		if datData[i] >  datData[i+1]:
			#swap!
			datData[i], datData[i+1] = datData[i+1], datData[i]
			i=0
			print datData
			
		else: 
			isSorted = True
	return True

def main():
	generateNums()
	#isSorted = bubbleSort(datData)
main()