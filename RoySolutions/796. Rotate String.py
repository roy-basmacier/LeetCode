class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        if len(B) != len(A):
            return False
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False