def longestRun(L):
    bestcount = 1
    bestlist = []
    for c in range(1, len(L)+1):
        temp = getSublists(L, c)
        print temp
        for lst in temp:
            count = 1
            for idx in range(len(lst)-1):
                if lst[idx+1] >= lst[idx]:
                    count += 1
                else:
                    count = 1
                    break
            if count > bestcount:
                bestcount = count
                bestlist = lst
            print bestcount, bestlist
    return bestcount
                 
