# 1365. How Many Numbers Are Smaller Than the Current Number
#
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]
# Return the answer in an array.
#
# Example 1:
#
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:
#
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:
#
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        memo = {}
        ans = []
        nnums = sorted(nums) # [1,2,2,3,4,5,6]
        for i in nnums :
            memo[i] = memo.get(i,0) + 1
            if i > memo.
        # print(memo) {1: 1, 2: 2, 3: 1, 8: 1}
        for i in nums:
            if i > memo.keys():
                print(memo.values())

            print(i)








s = Solution()
s.smallerNumbersThanCurrent([8,1,2,2,3])





