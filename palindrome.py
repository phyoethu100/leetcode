# Strings Question #6 - Palindrome
import re

def palindrome1(string):  # Pointer from left and right
    string = re.sub("[^A-Za-z0-9]", "", string).lower()
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False

    return True

# Time complexity: O(n)
# Space complexity: O(1)
print("Solution 1...")
print(palindrome1("A man, a plan, a canal: Panama"))
print(palindrome1("abba"))
print(palindrome1("aba"))
print(palindrome1("abc"))
print(palindrome1("a"))
print(palindrome1(""))


def palindrome2(string):  # Pointer from mid
    string = re.sub("[^A-Za-z0-9]", "", string).lower()
    mid = len(string) // 2 

    if len(string) % 2 == 0:  
        left = mid - 1
        right = mid
    else:
        left = mid
        right = mid 

    while left >= 0 and right < len(string):
        if string[left] == string[right]:
            left -= 1
            right += 1
        else:
            return False

    return True

# Time complexity: O(n)
# Space complexity: O(1)
print("Solution 2...")
print(palindrome2("A man, a plan, a canal: Panama"))
print(palindrome2("abba"))
print(palindrome2("aba"))
print(palindrome2("abc"))
print(palindrome2("a"))
print(palindrome2(""))


def palindrome3(string):  # Reverse strings
    string = re.sub("[^A-Za-z0-9]", "", string).lower()
    reverse = string[::-1]

    if string != reverse:
        return False

    return True

# Time complexity: O(n)
# Space complexity: O(1)
print("Solution 3...")
print(palindrome3("A man, a plan, a canal: Panama"))
print(palindrome3("abba"))
print(palindrome3("aba"))
print(palindrome3("abc"))
print(palindrome3("a"))
print(palindrome3(""))