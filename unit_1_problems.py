s = 'bobseriobobobewgboboeijklwjfbob'

# 1
vowels = 'aeiou'
vowel_count = 0

for char in s:
  if char in vowels:
    vowel_count += 1

print('Number of vowels: ' + str(vowel_count))

# 2
target_str = 'bob'
target_count = 0

for i in range(len(s) - len(target_str) + 1):
  test_str = s[i:(i + len(target_str))]
  if test_str == target_str:
    target_count += 1;

print('Number of times ' + target_str + ' occurs is: ' + str(target_count))

# 3

alph = 'abcdefghijklmnopqrstuvwxyz'

longest_str = s[0]
test_str = ''
prev_idx = alph.find(s[0])

for char in s:
  char_idx = alph.find(char)
  if char_idx < prev_idx:
    test_str = char
  else:
    test_str += char
    if len(test_str) > len(longest_str):
      longest_str = test_str

  prev_idx = char_idx

print('Longest substring in alphabetical order is: ' + longest_str)