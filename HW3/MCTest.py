from Generator import *
from Point import *
import math

def Scale(list):
    minList = min(list)
    maxList = max(list)

    for i in range(len(list)):
        list[i] = float(2*((list[i]-minList)/(maxList-minList))-1)        #scaling formula
    return list

def makePoint(x,y):
    list = []
    for i in range(len(x)):
        list.append(RectangularCoordinate(x[i], y[i]))
    return list
xGen = LCG(5, 1103515245, 12345, 2**32)
yGen = SCG(2, 1103515245, 12345, 2**32)

xList = Scale(xGen.giveSequence(10000000))
yList = Scale(yGen.giveSequence(10000000))

pointList = makePoint(xList,yList)

#print(xList)       #Code works
#print(pointList)    #Point objects were printed out which is okay
counter = 0
for i in pointList:
    if (i.Distance() < 1):
        counter += 1

print("The ratio of points inside the circle to the total is: ", (counter/10000000))
print("The difference between the theoretical ratio and the calculated ratio is: ", abs((counter/10000000)-(math.pi/4)))
