class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1

        for ch in s:
            if ch == '[' or ch == '(' or ch == '{':
                stack.append(ch)
                top += 1
            else:
                if top == -1:          # Empty stack
                    return False

                if (ch == "]" and stack[top] != '[') or \
                   (ch == "}" and stack[top] != '{') or \
                   (ch == ")" and stack[top] != '('):
                    return False

                stack.pop()            # Remove matched opening bracket
                top -= 1

        return top == -1