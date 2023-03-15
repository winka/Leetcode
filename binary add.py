# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        # 這樣迴圈不用往回跑
        a = a[::-1]
        b = b[::-1]
        print(a)
        print(b)
        # 選大的長度來做
        for i in range(max(len(a), len(b))):
            print(f'第{i}:')
            # 沒有值的話補 0
            # 三元運算
            # express1 if  else express2
            # 等於
            # if ?? :
            #   express1
            # else:
            #   express2
            a_bit = int(a[i]) if i < len(a) else 0
            b_bit = int(b[i]) if i < len(b) else 0
            print(f'a_bit:{a_bit}')
            print(f'b_bit:{b_bit}')
            print(f'carry:{carry}')
            s = a_bit + b_bit + carry
            print(f's:{s}')
            result += str(s % 2)
            print(f'result:{result}')
            carry = s // 2
            print(f'carry:{carry}')
        # 額外的 carry
        if carry:
            print('in if carry')
            print(result)
            print(carry)
            result += str(carry)
        # return 把值倒過來
        return result[::-1]
s = Solution()
s.addBinary(a = "1010", b = "1011")
# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return bin(eval(str(int(a,2) + int(b,2))))
#
# s = Solution()
# s.addBinary(a = "1010", b = "1011")
# a = "1010"
# a = a[::-1]
# print(a)