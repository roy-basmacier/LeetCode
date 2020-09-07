class Solution(object):
        
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # keep a dictionary of the frequency of each word, (string->int)
        
        # sort the dictionary according to the values (int) in accending order
        # same frequency should also be sorted to the lexicographical order
        # OR
        # make a min heap of y
        
        freq = {} # string -> int (word -> count)
        for word in words:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1
        
        heap = []

        for word, count in freq.items():
            heap.append((-count, word))
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res