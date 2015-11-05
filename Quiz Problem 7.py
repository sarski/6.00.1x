def uniqueValues(aDict):
    '''
    aDict: a dictionary
    
    Function that returns a list of keys in aDict that map to integer values 
    that are unique (i.e. values appear exactly once in aDict). The list of keys 
    you return should be sorted in increasing order. (If aDict does not contain 
    any unique values, you should return an empty list.)
    '''
    result = []
    count = 0
    for key in aDict.keys():
        for value in aDict.values():
            print 'key: ', key, 'value: ', value
            if aDict[key] == value:
                count += 1
        if count == 1:
            result.append(key)
        print 'count: ', count, 'resulting list: ', result
        count = 0
    result.sort()
    return result