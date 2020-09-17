class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Time  Complexity -> O(n)
        # Space Complexity -> O(n)
        freq = {}
        for ch in chars:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        cnt = 0
        for word in words:
            temp_freq = {}
            for ch in word:
                if ch in temp_freq:
                    temp_freq[ch] += 1
                else:
                    temp_freq[ch] = 1
            valid = True
            for key in temp_freq.keys():
                if key not in freq or temp_freq[key] > freq[key]:
                    valid = False
                    break
            if valid:
                cnt += len(word)
        return cnt