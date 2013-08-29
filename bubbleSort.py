
datData = [1,3,25,18,54,2,77,16,18,19,20,32,10,43,33,46,100,165,1024,566,343,23,45]

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
	isSorted = bubbleSort(datData)
main()