# 771. Jewels and Stones
#
#
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are casesensitive, so "a" is considered a different type of stone from "A".
# Example 1:
#
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
#
# Input: jewels = "z", stones = "ZZ"
# Output: 0


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        finder = {}
        counter = 0
        for i in stones :
            # dict.get(key, value) value 選填 如果 value 不存在 返回默認值
            finder[i] =  finder.get(i,0) + 1

        for i in jewels :
            counter+=finder.get(i,0)
        return counter
s = Solution()
s.numJewelsInStones(jewels = "aA", stones = "aAAbbbb")