word = 'bob'
count = 0
for idx in range(len(s)):
    if s[idx: (idx + 3)] == word:
        count += 1
print 'Number of times bob occurs is: ', count