def is_palindrome(s):
    s = s.lower().replace(' ', '')  # Convert to lowercase and remove spaces
    return s == s[::-1]

word = 'A man a plan a canal Panama'
if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')