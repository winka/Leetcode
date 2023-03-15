# 46. Permutations
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        temp = []
        for i in nums:
            temp.append(i)
            if len(temp) == 3 :
                ans.append(temp)
                temp = []
        def repeat(alist):
            for i, val in enumerate(nums):
                if val not in alist :
                    alist.append(val)


            pass


s = Solution()
s.permute([1,2,3])
