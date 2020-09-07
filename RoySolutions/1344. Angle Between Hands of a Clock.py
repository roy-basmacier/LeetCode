class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        # convert the minutes and hours to radian
        # M = m * 6 % 360
        # H = h * 5 * 6 % 360 + M
        # Answer = max(H,M) - min(H, M)
        
        M = (minutes * 6.0) %360
        H = ((hour * 30.0) % 360)  + minutes/2.0
        upper = max(H,M) - min(H,M)
        if upper > 180:
            return 360 - upper
        return upper