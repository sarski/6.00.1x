def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for item in aDict.values():
        for subitem in item:
            count += 1
    return count
