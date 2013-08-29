import random

#datData = [1,3,25,18,54,2,77,16,18,19,20,32,10,43,33,46,100,165,1024,566,343,23,45]

def generateNums():
	global f
	f = open("numbers.txt", 'w')
	nums = []
	for i in random.sample(range(500),500):
		nums.append(i)
	f.write('%s' % nums)

	#print nums
	return f
	#f.close()

def bubbleSort(f2):
	global isSorted
	isSorted = False
	f2 = open("numbers.txt", 'r')
	datData = []
	for x in f2:
		datData.append(x)
		print datData
	for i in range(len(datData)-1):
		if datData[i] >  datData[i+1]:
			#swap!
			datData[i], datData[i+1] = datData[i+1], datData[i]
			#i=0
			print datData
			
		else: 
			isSorted = True
	return True

def main():
	generateNums()
	isSorted = bubbleSort(f)
main()