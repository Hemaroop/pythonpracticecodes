def palinCheck(inStr):
    N = len(inStr)
    halfLen = 0
    subStr1 = ''
    subStr2 = ''

    i = 0
    diff = 0
    
    if (N%2 == 1):
        halfLen = int((N-1)/2)
        subStr1 = inStr[:halfLen]
        subStr2 = (inStr[halfLen + 1:])[::-1]
    else:
        halfLen = int(N/2)
        subStr1 = inStr[:halfLen]
        subStr2 = (inStr[halfLen:])[::-1]

    while i < halfLen:
        if subStr1[i] != subStr2[i]:
            diff = diff + 1
        if diff > 2:
            print("No")
            return 1
        i = i + 1

    print("Yes")
    return 0

inputString = input()
palinCheck(inputString)
        
