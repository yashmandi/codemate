def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

# Example usage:
print(is_palindrome("Racecar"))  # True
print(is_palindrome("hello"))    # False