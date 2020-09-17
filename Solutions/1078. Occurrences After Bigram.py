class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        # Time  Complexity -> O(n)
        # Space Complexity -> O(n)

        text = text.split(' ')
        res = []
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                res.append(text[i+2])
        return res
                