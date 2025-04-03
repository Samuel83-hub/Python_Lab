def count_vowels(s):
    return len(list(filter(lambda char: char in "aeiouAEIOU", s)))

print(count_vowels("Hello world"))
print(count_vowels("python"))
print(count_vowels("Beautiful Day"))
