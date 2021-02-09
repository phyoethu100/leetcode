# Stack Question #11 - Minimum Brackets to Remove

def minimum_bracket(string):
    res = list(string)
    stack = []

    for i in range (0, len(res)):
        if res[i] == "(":
            stack.append(i)
        elif res[i] == ")" and len(stack): 
            stack.pop()
        elif res[i] == ")":
            res[i] = ""
    
    while len(stack):
        cur_index = stack.pop()
        res[cur_index] = ""
    
    return "".join(res)



# Time complexity: O(4n) => O(n)
# Space complexity: O(2n) => O(n)
print(minimum_bracket('a)bc(d)'))
print(minimum_bracket('(ab(c)d'))
print(minimum_bracket('))(('))
print(minimum_bracket(')(a)bc)'))