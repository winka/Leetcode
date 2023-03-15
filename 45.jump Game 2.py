# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
#                  1 2 3 4
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2
# class Solution(object):
#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         ans = -1 # answer
#         pointer = 0 # now index
#
#         while True:
#             if nums[pointer] + pointer > len(nums):
#                 print(ans)
#                 return ans
#             else:
#                 # 一步範圍
#                 print('now in :' ,pointer)
#                 print('++',nums[pointer] + pointer)
#                 max_step_range = nums[pointer: nums[pointer] + pointer]
#                 print(max_step_range)
#
#                 # 範圍取最大
#                 maxx = max(max_step_range)
#                 print('max',maxx)
#                 a = nums.index(maxx)
#                 print('nums.index(maxx):', a)
#                 pointer += a
#
#                 print('after plus pointer:' ,pointer)
#                 print('_______________________________')
#                 ans += 1

# test = [2,3,1,1,4,7,6,2,4,67,]
# # print(max(test,key = lambda x: test[x]))
# max_test = test[:test[0]]
# print(max_test)
# # print()
# # 找到最大
# print(max(max_test, key = lambda x: x))
cur_far = 0 #end
            #far
     #i 0 1 2 3 4
nums = [2,3,2,5,4]
nums = [2,1,2,5,4]
for i in range(len(nums)-1):
    print('i:',i)
    print(max(cur_far,i+nums[i]))
# s = Solution()
# s.jump([4,3,0,1,4])