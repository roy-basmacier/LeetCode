class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        cnt = 0
        for dom in dominoes:
            if (min(dom),max(dom)) not in d:
                d[(min(dom),max(dom))] = 0
            else:
                d[(min(dom),max(dom))] += 1
                cnt += d[(min(dom),max(dom))]
        return cnt