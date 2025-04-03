def is_palindrome(s):

    s = s.replace(" ", "").lower()
    return s == s[::-1]


print(is_palindrome("malayalam"))    
print(is_palindrome("hello"))    
print(is_palindrome("racecar"))
