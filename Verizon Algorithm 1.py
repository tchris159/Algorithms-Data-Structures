# Write a program that finds the greatest difference between integers in a list. The list can contain positive and negative integers.
#
# Input:
# Your program should read lines from standard input. Each line contains a comma-separated list of integers.
#
# Output:
# For each input list, print to standard output the greatest difference between any two integers in the list. Print each difference on its own line.
#
# Test 1
# Test Input Download Test Input1,2,10,0,3,9
# Expected Output Download Test Output10
# Test 2
# Test Input Download Test Input4,-9,-3,0,7,9
# Expected Output Download Test Output18





from sys import stdin
line=stdin.readline().strip() #Read one line from console
l=line.split(',' ) #Split the line into a list via ,
ints=map(int,l)    #convert strings to ints
ints.sort()        #sort the ints from lowest to highest
print str(ints[-1]-ints[0]) #Find the Difference between biggest and smallest int
