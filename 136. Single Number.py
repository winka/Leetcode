# 136. Single Number
# Example 1:
#
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
#
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
#
# Input: nums = [1]
# Output: 1
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            if count.get(num, 0):  # Get value if duplicate, otherwise get default value of 0 and skip to else clause.
                print(num)
                print(count.get(num, 0))
                print(count)
                return True
            else:  # Update entry. Note we only ever need to count to 1 to detect duplicates.
                count[num] = 1
        return False

s = Solution()
s.singleNumber([2,2,1,2,3,6,7,84,6,78,11,2,456])