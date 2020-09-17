class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # Time  Complexity -> O(n)
        # Space Complexity -> O(1)

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True