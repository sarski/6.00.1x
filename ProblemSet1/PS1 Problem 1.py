vowels = 'aeiou'
count = 0
for letter in s:
    if letter in vowels:
        count += 1
print 'Number of vowels: ', count