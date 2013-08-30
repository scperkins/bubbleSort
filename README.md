bubbleSort
==========
A little challenege I made for myself.

An implementation of the dreaded bubble sort algorithm just for funsies. Generates a large list of randomly generated integers, with a 
range equal to the size of the list. To clarify, if the list has 100 indexes, it generates 100 random numbers from 0 to 99 
and appends them to the list.

It then writes that list to a txt file, reads the txt file back in, converts the numbers from a string back to the
original integers and plops them into a list again. This list is returned and sent to be sorted.

The list is run through the bubble sort algorithm contained within its own function and returns a sorted list.
The sorted list is the written to a new text file.
