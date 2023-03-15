# 209. Minimum Size Subarray Sum
# Example 1:
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
import sys


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 1
        rangesize = sys.maxsize
        while l < len(nums)+1  and r < len(nums)+1 :
            summ = sum(nums[l:r])

            if summ < target:

                if r == len(nums)+1: break

                r += 1

            elif summ >= target:
                if len(nums[l:r]) < rangesize:
                    rangesize = len(nums[l:r])
                l += 1



        return rangesize if rangesize < sys.maxsize else 0



s = Solution()
s.minSubArrayLen(7,[2,3,1,2,4,3])





