'''
prolem statement can be found at: 
https://code.google.com/codejam/contest/dashboard?c=2974486#s=p1
'''

def findRemainingTime(rate, X, C, F):
    totalTime = 0
    while(1):
        timeToBuyFarm = C / rate
        if X/rate < timeToBuyFarm + X/(rate + F):
            totalTime += X/rate
            return totalTime
        else:
            totalTime += C / rate #Increase the time remaining by the time to buy a farm.
            rate += F


inFile = open("B-large.in", "r")
outFile = open("output.txt", "w")

numTests = int(inFile.readline())

for i in range (numTests):
    values = (inFile.readline().rstrip()).split(" ")
    C = float(values[0])
    F = float(values[1])
    X = float(values[2])
    result = findRemainingTime(2, X, C, F)
    outFile.write("Case #{}: {}\n".format(i+1, result))
