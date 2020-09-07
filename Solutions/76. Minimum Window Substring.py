class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        s_count = {}
        TOTAL_S = {}
        for ch in t:
            if ch not in t_count:
                t_count[ch] = 1
                s_count[ch] = 0
                TOTAL_S[ch] = 0
            else:
                t_count[ch] += 1
                
                
                
        for ch in s:
            if ch in t_count:
                TOTAL_S[ch] += 1
        
        for k in t_count.keys():
                if t_count[k] > TOTAL_S[k]:
                    return ""
        
        #finding L's position
        L = -1
        for i in range(len(s)):
            if s[i] in t_count:
                L = i
                s_count[s[i]] += 1
                break
        if L == -1:
            return ""
        
        #finding R's position
        R = L
        for i in range(L+1,len(s)):
            if s[i] in t_count:
                R = i
                s_count[s[i]] += 1
            
            foundAll = True
            for k in t_count.keys():
                if t_count[k] > s_count[k]:
                    foundAll = False
                    break
            if foundAll:
                break
                
        if R == L:
            for k in t_count.keys():
                if t_count[k] > s_count[k]:
                    return ""
        
        minws = s[L:R+1]
        #4324
        for i in range(L, R):
                if s[i] in t_count:
                    if s_count[s[i]] - 1 < t_count[s[i]]:
                        L = i
                        break
                    else:
                        s_count[s[i]] -= 1
            
        if len(s[L:R+1]) < len(minws):
            minws = s[L:R+1]
            
        
        
        while(1):
            prvR = R
            # moving R so it's at L's character
            for i in range(R+1,len(s)):
                if s[i] in t_count:
                    s_count[s[i]] += 1

                if s[i] == s[L]:
                    R = i
                    break
            # checking if we found a new place for R
            if prvR == R:
                break
            
            #reducing L
            for i in range(L, R):
                if s[i] in t_count:
                    if s_count[s[i]] - 1 < t_count[s[i]]:
                        L = i
                        break
                    else:
                        s_count[s[i]] -= 1
            
            if len(s[L:R+1]) < len(minws):
                minws = s[L:R+1]
            

        #asd
        for i in range(L, R):
                if s[i] in t_count:
                    if s_count[s[i]] - 1 < t_count[s[i]]:
                        L = i
                        break
                    else:
                        s_count[s[i]] -= 1

        if len(s[L:R+1]) < len(minws):
            minws = s[L:R+1]
        
        
        for i in range(L, R):
                if s[i] in t_count:
                    if s_count[s[i]] - 1 < t_count[s[i]]:
                        L = i
                        break
                    else:
                        s_count[s[i]] -= 1

        if len(s[L:R+1]) < len(minws):
            minws = s[L:R+1]
       
                
        return minws