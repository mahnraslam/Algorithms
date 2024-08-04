# Stack

# 1. for ss in s
#     if s is left, put it into stack
#     if s is right, pop stack, check whether these two match
# 2. return if stack is empty

# TC: O(n)
# SC: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(':')', '[':']', '{':'}'}

        for ss in s:
            if ss in ('(', '[', '{'):
                stack.append(ss)
            elif not stack or pair[stack.pop()] != ss:
                return False
            
#Solution2

class Solution:
    def isValid(self, string: str) -> bool:
        brackets = {"(":")", "{":"}" , "[":"]"}
        s = []
        for i in string:
            if i in brackets:  # If it's an opening bracket
                s.append(i)
            elif i in brackets.values():
                if not s  or brackets[s.pop()] != i  :
                    return False
            else :
                s.append(i)
        return len(s) == 0