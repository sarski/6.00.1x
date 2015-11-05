def isIn(char, aStr):
    if aStr == '':
        return False
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    mid = len(aStr) / 2
    if char == aStr[mid]:
        return True
    else:
        if char > aStr[mid]:
            return isIn(char, aStr[mid:])
        else:
            return isIn(char, aStr[:mid])