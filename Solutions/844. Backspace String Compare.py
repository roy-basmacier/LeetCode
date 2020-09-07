class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS = []
        stackT = []
        for ch in S:
            if ch == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(ch)
        for ch in T:
            if ch == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(ch)
        if stackT == stackS:
            return True
        return False