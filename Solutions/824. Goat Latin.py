class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)
        def isVowel(ch):
            vowels = "aeiouAEIOU"
            return ch in vowels
            
        S = S.split(" ")
        for i in range(len(S)):
            aCount = i + 1
            word = S[i]
            
            if isVowel(word[0]):
                word += "ma"
                
            else:
                word = word[1:] + word[0] + "ma"
            
            word += "a" * aCount
            S[i] = word
        return " ".join(S)
            
                