def genPrimes():
    ans = []
    yield 2
    ans.append(2)
    next_val = 3
    while True:
        isPrime = True
        for idx in range(len(ans)):
            if next_val % ans[idx] == 0:
                isPrime = False
        if isPrime:    
            yield next_val
            ans.append(next_val)
        next_val += 1