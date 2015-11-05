def primesList(N):
    '''
    N: an integer
    '''
    result = []
    is_prime = True
    for number in range(2, N + 1):
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            result.append(number)
    return result