# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Example
# 1:
#
# Input: nums = [3, 2, 3]
# Output: [3]
# Example
# 2:
#
# Input: nums = [1]
# Output: [1]
# Example
# 3:
#
# Input: nums = [1, 2]
# Output: [1, 2]
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list1 = list(set(nums))
        ans = [i for i in list1 if nums.count(i) > len(nums)/3]
        return ans

s = Solution()
s.majorityElement([1, 2])
# print(  type(list(set([3, 2, 3]))))
