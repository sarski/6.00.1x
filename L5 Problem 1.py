def iterPower(base, exp):
    result = 1
    for idx in range(exp):
        result *= base
    return result