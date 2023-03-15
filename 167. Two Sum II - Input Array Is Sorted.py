# 167. Two Sum II - Input Array Is Sorted

# Example 1:
# Input: numbers = [0,1,2,3,4,5,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [1,2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        right, left = len(numbers)-1, 0
        while right > left :
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1,right+1]
            elif sum > target:
                right-=1
            else:
                left+=1
    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        # dict={val, index}
        for i, val in enumerate(numbers):
            if target-val in dict :
                return [dict[target-val]+1, i+1]
            dict[val] = i




s = Solution()
s.twoSum([0,0,3,4],0)
s.twoSum2([0,0,0,3,4],0)
# print(list(set([1,2,3,3,4,5,5,5])))
#
# print([1,2,3,3,4,5,5,5].index(9)) # return first number in list

# Return double of n
def addition(n):
    return n + n if n >= 5 else n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

