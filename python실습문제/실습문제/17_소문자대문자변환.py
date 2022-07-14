# print(ord('a'))
# print(ord('A'))
# print(ord('b'))
# print(ord('B'))
# print(ord('c'))
# print(ord('C'))

# print(97-65)

# x = ord('a') - 32
# print(chr(x))

word = 'banana'
change = 0
new_word = ''

for i in word:
   change = ord(i) - 32
   new_word += chr(change)

print(new_word)