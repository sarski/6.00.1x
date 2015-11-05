def count7(N):
    '''
    N: a non-negative integer
    use recursion
    '''
    count = 0
    if N % 10 == 7:
        count += 1
    if N / 10 == 0:
        return count
    return count + count7(N / 10)