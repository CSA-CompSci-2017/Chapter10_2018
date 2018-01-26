#Andrew Hilton 4th pd comp sci 1/23/18, absent on monday
import random
x=76
y=92.3
z="hello"
w=True
k=76
myList = []
myList.append(x)
myList.append(y)
myList.append(z)
myList.append(w)
myList.append(k)
print(myList)
myList = []
myList = myList + [x]
myList = myList + [y]
myList = myList + [z]
myList = myList + [w]
myList = myList + [k]
print(myList)
newList=[]
for a in range(100):
    b = random.randrange(0, 1001)
    newList.append(b)
print(newList)
def average(newList):
    avgList = []
    for m in newList:
        newList.append(x/100)
    print(newList)
average(newList)
