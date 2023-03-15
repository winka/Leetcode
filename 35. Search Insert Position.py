# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Example1:
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2

# Example2:
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1

# Example3:
# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search
        l, now, r = 0, len(nums)//2, len(nums) - 1
        while True :
            # find

            if target in nums:
                return nums.index(target)
            elif target < nums[l] :
                return 0
            elif target > nums[r] :
                return len(nums)

            if  nums[now] <= target <= nums[now+1]:
                if nums[now] == target :
                    return now
                return now + 1
            # to right
            elif target > nums[now] :
                now = (now + r)//2
            # to left
            elif target < nums[now]:
                now = (now + l)//2



s = Solution()
s.searchInsert(nums = [1, 3, 5, 6], target = 5)


          #0 1 2 3 4 5 6
# print(len([1,2,3,4,5,6,7],2))
# print(len([1,2,3,4,5,6])//2)





