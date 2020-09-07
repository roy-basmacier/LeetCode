class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # My approach is to iterate through the input and store the variables in a stack
        # when we see a C we will try to pop the previous number
        # when we see a D we will try pop the previous number nad double i and push it back
        # when we see a + we will try to pop last two elements and add them and push it back
        # at the end we will pop all the numbers in out stack and sum it up and return it
        stack = []
        for ch in ops:
            if ch == "C":
                if stack != []:
                    stack.pop()
            elif ch == "D":
                if stack != []:
                    stack.append(stack[-1] * 2)
            elif ch == "+":
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(ch))
        
        return sum(stack)