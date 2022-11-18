class Solution(object):
    def runningSum(self, nums):
        
        output = []
        
        for i, v in enumerate(nums):
            j = v + sum(nums[:i])
            output.append(j)
        
        return output
