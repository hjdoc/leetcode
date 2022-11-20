class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        input = num
        count = 0
        while input > 0:
            if input % 2 == 0:
                input = input / 2
                count += 1
            else:
                input = input - 1
                count += 1
        return count

