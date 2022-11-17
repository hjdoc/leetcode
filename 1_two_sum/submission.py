class Solution(object):
    def twoSum(self, nums, target):

        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in nums and nums.index(remaining) != i:
                n = nums.index(remaining)
                return [i, n]
