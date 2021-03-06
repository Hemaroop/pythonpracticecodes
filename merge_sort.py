def splitList(numList):
    listLen = len(numList)
    halfLen = 0

    if (listLen%2 == 1):
        halfLen = int((listLen+1)/2)
    else:
        halfLen = int(listLen/2)

    return numList[:halfLen], numList[halfLen:]

def listSort(numList):
    if len(numList) == 2 and numList[0] > numList[1]:
        return numList[::-1]
    else:
        return numList
    
def mergeSortedLists(firstList,secondList):
    outList = []
    i = 0
    j = 0

    while i < len(firstList):
        while j < len(secondList):
            if i < len(firstList):
                if firstList[i] < secondList[j]:
                    outList.append(firstList[i])
                    i = i+1
                else:
                    outList.append(secondList[j])
                    j = j+1
            else:
                outList.append(secondList[j])
                j = j+1

        if i < len(firstList):
            outList.append(firstList[i])
            i = i + 1

    return outList
    
def mergeSort(numList):

    if len(numList) > 2:
        fHalfList,sHalfList = splitList(numList)
        sortedfHalfList = mergeSort(fHalfList)
        sortedsHalfList = mergeSort(sHalfList)
        return mergeSortedLists(sortedfHalfList,sortedsHalfList)
    else:
        return listSort(numList)

nOfInts = int(input("Number of items in list:"))
numList = []
while (nOfInts > 0):
    inputNum = int(input("Enter a number:"))
    numList.append(inputNum)
    nOfInts = nOfInts - 1

outputList = mergeSort(numList)
print(outputList)
    
