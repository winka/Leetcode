class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo = {}
        for i,val in enumerate(nums):
            if target-val in memo :
                print([memo[target-val], i])
                return [memo[target-val], i]
            memo[val] = i



s = Solution()
s.twoSum(nums = [3,0,0,0,3], target = 6)