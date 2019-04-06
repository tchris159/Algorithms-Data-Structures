
'''

INST326 Object-Oriented Programming
Section 0201
Homework 5 Resubmission
Christopher Truong
Fall 2017

'''



def consChars(file_name):          #takes file as an argument for parsing data
    count =0
    w = open('words.txt','w')
    file = open(file_name, 'r')
    for line in file:
        line = line.rstrip()      #goes through each line in text file to get rid of white space
        is_c = h1(line)
        if is_c == True:
            w.write(line)
            count = count +1          #records count for the number of lines
    w.close()
    file.close()
    return count

def h1(word):
    for index in range(len(word)):
        if index == 0:
            continue
        if(word[index]==word[index-1]):      #if the index is equal to the index before return true for that word
            return True
        else:
            continue