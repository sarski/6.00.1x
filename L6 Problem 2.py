def oddTuples(aTup):
    result = ()
    for idx in range(len(aTup)):
        if not idx % 2:
            result += (aTup[idx], )
    return result