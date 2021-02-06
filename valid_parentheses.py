# Stack Question #10 - Valid Parentheses

parens = {
    '(': ')',
    '[': ']',
    '{': '}'
}

def valid_parentheses(string):
    
    if len(string) == 0:
        return True
    
    stack = []

    for i in range(0, len(string)):
        if parens.get(string[i]) != None:
            stack.append(string[i])
        else:
            left_bracket = stack.pop() 
            correct_bracket = parens[left_bracket]

            if string[i] != correct_bracket:
                return False
    
    return len(stack) == 0


# Time complexity: O(n)
# Space complexity: O(n)
print(valid_parentheses('[{()}]'))
print(valid_parentheses('[{}()]'))
print(valid_parentheses('[{(})]'))
print(valid_parentheses('[{()'))
print(valid_parentheses('['))
print(valid_parentheses(''))
