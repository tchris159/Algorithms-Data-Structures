"""
You are playing a game with several friends. Each of your friends chooses a number between 1 and 9 (inclusive) and writes it down
on a piece of paper.
You, as the judge, collect all the papers and must determine the winner. The winner of the game is the player who submitted the 
lowest unique number.
There are 10-20 players in the game.

Input:
Your program should read lines from standard input. You are the judge, and you're given a set of space-delimited numbers from players for each round of game.

Output:
Print the winner's position in the input list, or 0 if there is no winner (there are no unique numbers). 
In the first sample test case, the lowest unique number is 6. So player 5 wins.

Test 1

Test Input: 3 3 9 1 6 5 8 1 5 3
Expected Output: 5

Test 2

Test Input: 9 2 9 9 1 8 8 8 2 1 1
Expected Output: 0
"""

# first read from console, split the strings based on spaces, then convert to integers and then sort. 

from sys import stdin
print "Enter data:"
line=stdin.readline().strip() #Read one line from console
l=line.split(' ' ) #Split the line into a list via ' '
ints=map(int,l)    #convert strings to ints
intscopy=ints+[]
ints.sort()        #sort the ints
##^^Above code is largely reused, except we split by ' ' and not ','


# while loop that checks if the current element is equal to the next because it is sorted. Keep assigning value to the next int if there
# are duplicates break  

position=0
#Now that we sorted the list, it is NOT unique then i[p]=i[p+1].
while (ints[position]==ints[position+1]):
    value=ints[position]
    #Since it is not unique, we go to the next number.
    #We have to increment position for as many times as there are duplicates
    try:
        while (value==ints[position]):
            position+=1
    except:
            break
#The while loop above stops when we found a unique number.
#Since it is also the smallest number, it is the smallest unique number.
if position<len(ints):
    lowestuniq=ints[position]
    #But that is not what we want...we want the position in the original list.
    count=0
    for x in intscopy:
        if x==lowestuniq:
            print count+1
        count+=1
else:
    print 0
