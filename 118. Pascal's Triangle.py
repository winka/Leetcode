# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:24:34 2022

@author: user

class Solution:
    def generate(self,numRows):
        pascal = [[1]*(i+1) for i in range(numRows)]
        #print(pascal[-1])
        
        
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
                print("i j ",i,j)
                print(pascal)
                print("==========================================")
        return pascal
              
      
s = Solution()
s.generate(4)

"""

class Solution:
     def generate(self, numRows):

        total_list = []
        now_list = []
        last_list = []
        
         
        for num in range(numRows):
            
            right = num
            left = 0
            
            if left == 0 :

                if right == 0:      #right= num+1 可省略?
                    total_list.append([1])
                    continue
                else:
                    left += 1
                    now_list.append(1)

            while left < right:#迴圈while
                
                number = last_list[left-1] + last_list[left]
                now_list.append(number)
                left += 1
               
            
        
            if left == right:
                now_list.append(1)
                last_list = now_list         
                total_list.append(now_list)
                now_list=[]
        
        return total_list
                
        
        
        
s = Solution()

s.generate(5)