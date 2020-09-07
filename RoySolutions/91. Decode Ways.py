class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(i, s, memo):
            if memo[i] > -1:
                return memo[i]
            if s[i] == '0':
                memo[i] = 0
                return 0
            cnt = helper(i+1, s, memo)
            if i < len(s)-1 and int(s[i:i+2]) < 27:
                cnt += helper(i+2, s, memo)
            memo[i] = cnt
            return cnt
        
        memo = [-1] * (len(s)+1)
        memo[len(s)] = 1
        return helper(0, s, memo)
        