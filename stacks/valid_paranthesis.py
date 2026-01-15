'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        brack_map = {"(": ")", "[": "]", "{": "}"}
        brack_inverse_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for brack in s:
            if brack in brack_inverse_map and stack and stack[-1] == brack_inverse_map[brack]:
                stack.pop()
            elif brack in brack_inverse_map and stack and stack[-1] != brack_inverse_map[brack]:
                return False
            elif brack in brack_inverse_map and not stack:
                return False
            else:
                stack.append(brack)
        return not stack
    
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))