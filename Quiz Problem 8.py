def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    cloneL = list(L)
    #items_to_remove = []
    for item in cloneL:
        if not f(item):
            L.remove(item)
    return len(L)
    
def f(s):
    return 'a' in s    

# run_satisfiesF(L, satisfiesF)