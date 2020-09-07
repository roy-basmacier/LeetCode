class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        result = 0
        cnt = 0
        i = 0
        while(i < len(s)):
            if s[i] not in d:
                d[s[i]] = i
                cnt += 1
            else:
                if cnt > result:
                    result = cnt
                
                i = d[s[i]]
                d = {}
                cnt = 0
            i += 1
        if cnt > result:
            return cnt
        return result