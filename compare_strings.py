# Strings Question #4 - Typed Out Strings

def build_string(string):
    result = []

    for i in range(0, len(string)):
        if string[i] != "#":
            result.append(string[i])
        elif string[i] == "#" and len(result) != 0:
            result.pop()

    return result

def compare_strings(s, t):

    final_s = build_string(s)
    final_t = build_string(t)

    if len(final_s) != len(final_t):
        return False 
    else: 
        for i in range(0, len(final_s)):
            if final_s[i] != final_t[i]:
                return False

    return True
   
# Time complexity: O(a+b)
# Space complexity: O(a+b)
print("Brute force solution...")
print(compare_strings("ab#z", "az#z"))
# print(compare_strings("a######z", "bz##z"))
# print(compare_strings("a####z#", "#z#a#"))
# print(compare_strings("###z#a", "#z#a#a"))


def improved_compare_strings(s, t):
    p1 = len(s) - 1
    p2 = len(t) - 1 

    while p1 >= 0 or p2 >= 0:
        if s[p1] == "#" or t[p2] == "#":
            if s[p1] == "#":
                backcount = 2
                while backcount > 0:
                    p1 -= 1
                    backcount -= 1 
                    if s[p1] == "#":
                        backcount += 2
                
            if t[p2] == "#":
                backcount = 2
                while backcount > 0:
                    p2 -= 1
                    backcount -= 1
                    if t[p2] == "#":
                        backcount += 2
        else:
            if s[p1] != t[p2]:
                return False 
            else:
                p1 -= 1
                p2 -= 1
    
    return True 

# Time complexity: O(a+b)
# Space complexity: O(1)
print("Optimal solution...")
print(improved_compare_strings("ab#z", "az#z"))
# print(improved_compare_strings("abc#d", "abzz##d"))
# print(improved_compare_strings("ab##", "c#d#")) - NOT WORKING