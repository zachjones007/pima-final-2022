global globalList, globalList1
globalList = []
globalList1 = [globalList]
b =2 
c = 3
a = [b,c] 

d = 4
class MyList():
    def __init__(self):
        self._myList = [a]

    @property
    def myList(self):
        return self._myList + globalList
    @myList.setter
    def myList(self, val):
        self._myList = val

    def append(self, val):
        self.myList = self.myList + [val]
        return self.myList  

    def extend(self, val):
        return self.myList.extend(val)


mL1 = MyList()
print("myList: ", mL1.myList)
mL1.append(4)
print("after appending a 4, myList: ", mL1.myList)
mL1.myList.extend([5,6,"eight","IX"])
print("after extend, myList: ", mL1.myList)