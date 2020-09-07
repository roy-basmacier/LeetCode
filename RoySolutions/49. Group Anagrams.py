class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for word in strs:
            unique = 0
            for ch in word:
                unique += ord(ch) ** 17
            if unique not in d:
                d[unique] = []
            d[unique].append(word)
        print(d)
        return d.values()