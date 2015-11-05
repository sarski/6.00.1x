def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    values = [len(items) for items in aDict.values()]
    maxval = max(values)
    for key, values in aDict.items():
        if len(values) == maxval:
            return key