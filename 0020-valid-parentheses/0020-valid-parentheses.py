# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []

#         for char in s:
#             if char == "(":
#                 stack.append(")")
#             elif char == "{":
#                 stack.append("}")
#             elif char == "[":
#                 stack.append("]")

#             else:
#                 if len(stack) == 0 or char != stack[-1]:
#                     return False
#                 stack.pop()

#         return  len(stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False
        return len(stack) == 0