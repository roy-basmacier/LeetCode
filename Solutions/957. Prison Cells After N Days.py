class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        pastCells = {str(cells): N}
        while N:
            pastCells[str(cells)] = N
            N -= 1
            temp = [0] * 8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    temp[i] = 1
                    
            if str(temp) in pastCells:
                N %= pastCells[str(temp)] - N
            cells = temp
        return cells
