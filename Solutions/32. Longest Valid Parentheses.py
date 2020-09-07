class Solution:
    def longestValidParentheses(self, s: str) -> int:
        current = 0
        maxlen = 0
        # *_(()_*
        # stack = (
        # current = 2
        # maxlen = 2
        stack = [-1]
        for i in range(len(s)):
            if (s[i]) == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack != []:
                    stack
                    current = i - stack[-1]
                    if current > maxlen:
                        maxlen = current
                else:
                    stack.append(i)

        return maxlen