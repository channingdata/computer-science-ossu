s = input("Please input any 1-part string: ")

vowels = ['a','e','i','o','u']

count_vowels = 0
for char in s:
    if char in vowels:
        count_vowels += 1

print('Number of vowels:', count_vowels)