class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0 for _ in range(i + 1)] for i in range(query_row + 2)]
        tower[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if tower[i][j] > 1:
                    tower[i+1][j] += (tower[i][j] - 1) / 2
                    tower[i+1][j+1] += (tower[i][j] - 1) / 2
        if tower[query_row][query_glass] > 1:
            return 1

        return tower[query_row][query_glass]