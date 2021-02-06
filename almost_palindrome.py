# Strings Question #6 - Almost Palindrome
import re

def almost_palindrome(string):
    string = re.sub("[^A-Za-z0-9]", "", string).lower()
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return sub_palindrome(string, left+1, right) or sub_palindrome(string, left, right-1)
        left += 1
        right -= 1

    return True

def sub_palindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False  
        left += 1
        right -= 1

    return True

# Time complexity: O(n)
# Space complexity: O(1)
print("Optimal solution...")
print(almost_palindrome("raceacar"))
print(almost_palindrome("abccdba"))
print(almost_palindrome("abcdefdba"))
print(almost_palindrome("a"))
print(almost_palindrome(""))
print(almost_palindrome("ab"))