class Solution(object):
    def twoSum(self, nums, target):

        open_list = list(enumerate(nums))
        # brute force
        while len(open_list) > 1:
            first = open_list.pop(0)
            for num in open_list:
                if first[1] + num[1] == target:
                    return [first[0], num[0]]

