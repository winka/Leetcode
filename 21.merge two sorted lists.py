# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
list1 = [], list2 = [0]
print(sorted(list1 + list2))
# s = Solution()
# s.mergeTwoLists(list1,list2)
