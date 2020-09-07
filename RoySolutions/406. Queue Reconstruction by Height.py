class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # find the shortest person and put that person in the correct posistion
        # ideal approach to sort the people array according to the height then their k value
        # pop shortest poistion repeat
        
        # [7,0], [4,4], [7,1], [5,0], [6,1], [5,2] => 
        # after sorting
        # [7,0], [7,1], [6,1], [5,0], [5,2], [4,4]
        
        # shortest: [4,4]
        # res: [None, None, None, None, [4,4], None]
        
        # shortest: [5,0]
        # res: [[5,0], None, None, None, [4,4], None]
        
        # shortest: [5,2]
        # res: [[5,0], None, [5,2], None, [4,4], None]
        
        # shortest: [6,1]
        # res: [[5,0], None, [5,2], [6,1], [4,4], None]  
        
        # shortest: [7,0]
        # res: [[5,0], [7,0], [5,2], [6,1], [4,4], None]  
        
        # shortest: [7,1]
        # res: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]  
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        for h, k in people:
            res.insert(k, [h, k])
        return res
        
        
        
        
        
        
        
        