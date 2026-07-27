class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def si(s):
            stack=[]
            for i in s:
                if i=='#':
                    if len(stack)>0:
                        stack.pop()
                else:
                    stack.append(i)
            return stack
        return si(s)==si(t)