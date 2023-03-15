# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j
# 4 6
# 3 3
# 2 1
# 1 0
# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums, memo = sorted(nums), {}  # sort to get the total number of digits that have duplicates
        for i in range(len(nums) - 1):  # lets say nums = [1,1,1,1,2,2,2,3] the total digits with duplicates is 7
            if nums[i] == nums[i + 1]:  # because nums has 4 ones and 3 twos so it adds up to 7
                if nums[i] not in memo:  # 3 is not counted because there are no duplicates of it
                    print('in if if')
                    memo[nums[i]] = 1
                print(nums[i])
                print('out side')
                memo[nums[i]] = memo[nums[i]] + 1
                print(memo)
        # nums = [1,1,1,1,2,2,2,3]
        # so now memo = {1 : 4, 2: 3} which means we have 4 ones and 3 twos
        answer = 0
        for n in memo.values():  # this is the hard part, please refer to my beautiful drawing to understand this
            answer += (n ** 2 - n) // 2  # after looking at the drawing, we repeat with each n value in memo
        print(answer)





s = Solution()
s.numIdenticalPairs([1,1,1,1,2,2,2,3])