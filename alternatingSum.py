def alternatingSum(a):
    sum = 0
    for i in range(len(a)-1): #len(a) is 3 range then evaluates to 0, 1, 2 ( everything up to but not including 3)
        if i % 2 == 0:
            sum = a[i] - a[i+1]
            sum = a[i+1]
        else:
            sum = a[i] + a[i+1]
            sum = a[i+1]
    return sum


print(alternatingSum([10, 20, 30]))

    #need to do operations based on index locations
    #if its even then do subtraction if odd do addition
    #similar to exam lists