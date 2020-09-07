class Solution(object):
    def isHappy(self, n):
        visited = set()
        while 1:
            if n in visited:
                return False
            visited.add(n)
            s = str(n)
            n = 0
            for ch in s:
                n += int(ch)**2
            if n == 1:
                return True

        