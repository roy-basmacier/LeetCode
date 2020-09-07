class Solution(object):
    
    def compare(self, arr1, arr2):
        for i in range(26):
            if arr1[i] != arr2[i]:
                return False
        return True
            
    
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        freq = [0 for i in range(26)]
        window = [0 for i in range(26)]
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
            
        
        for i in range(len(s2)-len(s1)):
            if self.compare(freq, window):
                return True
            window[ord(s2[i + len(s1)]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] -= 1
            
            

        return self.compare(freq, window)
                
            
            
            
            
            
        
        