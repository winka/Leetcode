# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:30:43 2022

@author: user

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        T0 ,T1, T2 = 0, 1, 1 
        count = 0 
        if  n == 0:
            count = T0
        elif n == 1:
            count = T1
        elif n == 2:
            count = T2
            
        else :
            for i  in range(n-2):
                count = T0 + T1 + T2
                T0 = T1
                T1 = T2
                T2 = count
        return count

         
        


s = Solution()
s.tribonacci(4)