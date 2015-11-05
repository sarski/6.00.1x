def lenIter(aStr):
    ans = 0
    while aStr != '':
        ans += 1
        aStr = aStr[ : -1]
    return ans
    
def lenIter2(aStr):
    ans = 0
    for char in aStr:
        ans += 1
    return ans