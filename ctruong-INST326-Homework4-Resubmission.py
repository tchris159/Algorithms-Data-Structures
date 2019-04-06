'''

INST326 Object-Oriented Programming
Section 0201
Homework 4 RESUBMISSION FOR STYLE 
Christopher Truong
Fall 2017

'''

def wordWrapper(text, length):
	high = length     #set length equal to high, so it can be later used in the while loop
	low = 0
	i = 0
	while(i<length):
		print(text[low:high])        #slice the text to the desired ending length, to direct program when to stop wrapping
		low = low + length
		high = high + length
		i = i+1                      #continues appending and wrapping text until desired result

#This is just to test this function
wordWrapper("python is cool", 4)