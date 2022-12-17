# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 19:53:14 2022

@author: user


from itertools import permutations
print(list(permutations("ABCD",2)))

'''
        if n%2 == 0: #奇偶判斷  並算出最少有幾個位置
            positon = n/2
            print("偶數")
            print("Positon:",positon)
        else:
            print("奇數")
            
            print("Positon:",positon)
        '''

"""

import math 

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #print("n",n)
        ways = 0 
        i = 0 #有幾個2
        positon = n #有幾個位置
        stop = int(n/2)  # 3:1  4:2  5:2 6:3
       
        
       
        if n == 1 : # 1
            ways =  1 
         # 1 2  3  4  5 
                        # 0 1  1  2 
        
        #print("stop :",stop)
        #print("i",i)
             # i=0  stop=1 
        while i <= stop and stop > 0:
            
            if n == 2 : #2 
                ways =  2
                #print(ways,"hello")
                break
            
             # 次方數 # 2以上  3 4 5
             
            else:                 #階乘 =  C N 取 M = N! / (M!(N-M!))
                ways = ways + int( math.factorial(positon)/(math.factorial(i)*math.factorial(positon-i)) ) # ways= 0 + 1      
                i = i + 1
                positon = positon - 1
                #print("i:",i)
                
                
        print(ways)





test = Solution()
test.climbStairs(5)

