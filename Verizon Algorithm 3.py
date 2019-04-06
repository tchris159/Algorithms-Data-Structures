from sys import stdin
line=stdin.readline().strip() #Read one line from console
line=line.lower() #set everything lower case
chars=list(line) #Make everything into one list of chars
chars.sort()
position=0
currentCount=0
currentChar=chars[0]
output=""
for c in chars:
    if currentChar==c:
        currentCount=currentCount+1 #add to the count of currentChar
    else:
        output=output+currentChar+str(currentCount) #output the count
        currentChar=c #now count the next unique char
        currentCount=1
output=output+currentChar+str(currentCount) #Do this for the last char
print output
