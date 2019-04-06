def doublePrices(d):
    for key, value in d.items():
        d[key]= value * 2
    return d
print(doublePrices({'a':1.0,'b':2.0}))





