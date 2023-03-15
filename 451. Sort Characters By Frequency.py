# 451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        nlist = list(s) # [t,r,e,e]
        word = {}
        ans = ''
        for i in s :
            word[i] = s.count(i)
        print(word) # {'t': 1, 'r': 1, 'e': 2}
        temp = []
        for i in nlist :
            if not i in temp:
                temp.append(i)
            # if big 往前插
            if word.get(i)>
            # else 往後插
            # if i in nword:
            #     ans += i
        print(ans)
        # return ans


# s = 'tree'
# print(s[0])
s = Solution()
s.frequencySort("tree")
