def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    else:
        if exp % 2:
            return base * recurPowerNew(base, exp - 1)
        else:
            return recurPowerNew(base * base, exp / 2)