# Strings Question #5 - Longest Substring without Repeating Characters

def longest_substring(string):

    longest = 0 

    if len(string) <= 1:
        return len(string)

    for left in range(0, len(string)):
        seen_chars = {}
        current_length = 0

        for right in range(left, len(string)):
            current_char = string[right]

            if seen_chars.get(current_char) == None:
                current_length += 1
                seen_chars[current_char] = True 
                longest = max(longest, current_length)
            else:
                break 
    
    return longest

# Time complexity: O(n^2)
# Space complexity: O(n)
print("Brute force solution...")
print(longest_substring("abcbdca"))
print(longest_substring("abccba"))
print(longest_substring("abcb"))


def improved_longest_substring(string):

    if len(string) <= 1:
        return len(string)

    left = 0
    longest = 0
    seen_chars = {}

    for right in range(0, len(string)):
        current_char = string[right]
        prev_seen_char = seen_chars.get(current_char)
        
        if current_char in seen_chars:
            if prev_seen_char >= left:
                left = prev_seen_char + 1
        
        seen_chars[current_char] = right
        longest = max(longest, right - left + 1)
        
    return longest

# Time complexity: O(n)
# Space complexity: O(n)
print("Optimal solution...")
print(improved_longest_substring("abcb"))
print(improved_longest_substring("abcbdca"))
print(improved_longest_substring("abcbdaac"))
print(improved_longest_substring("a"))
print(improved_longest_substring(""))