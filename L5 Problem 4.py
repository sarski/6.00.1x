def gcdIter(a, b):
    gcd = min(a, b)
    if gcd == 1:
        return gcd
    else:
        while a % gcd != 0 or b % gcd != 0:
            gcd -= 1
        return gcd