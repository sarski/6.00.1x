letter_order = 'abcdefghijklmnopqrstuvwxyz'
substr = ''
ans = ''
max_count = 0
length = 0
idx = 0
for letter in s:
    letter_idx = letter_order.index(letter)
    if letter_idx >= idx:
        substr += letter
        length += 1
    else:
        if length > max_count:
            max_count = length
            ans = substr
        substr = letter
        length = 1
    idx = letter_idx    
if len(ans) < len(substr):
    ans = substr
print 'Longest substring in alphabetical order is: ', ans