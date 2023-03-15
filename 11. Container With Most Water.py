# 11. Container With Most Water
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Input: height = [1,1]
# Output: 1

class Solution:
    def maxArea(self, H: List[int]) -> int:
        class Solution:
            def maxArea(self, H: List[int]) -> int:
                ans, i, j = 0, 0, len(H) - 1
                while (i < j):
                    if H[i] <= H[j]:
                        res = H[i] * (j - i)
                        i += 1
                    else:
                        res = H[j] * (j - i)
                        j -= 1
                    if res > ans: ans = res
                return ans

s = Solution()
s.maxArea([4,3,2,1,4])
