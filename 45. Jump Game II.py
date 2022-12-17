# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:44:17 2022

@author: user
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
       
        #print(max(nums[0 : 2]))  #結果 2 3 
        def jumpper(start_point, nums_list, summ, step ,goal): # 目前在的地方 ,目前可以走的步數 , 加起來                         
            
                        # 0                 nums[0]
            end_point = start_point + nums[start_point] 
            print("start point ",start_point)
            print("end point " , end_point)
           
            #print(max(nums_list))      # 1         :    2
            summ = summ + max(nums_list[start_point : end_point])
            print("sum ",summ)          #[1:3]
            
            p = nums_list.index(max(nums_list[start_point+1 : end_point+1])) #最大數位置
            step += 1 
            print("p",p)
            print("------------------------------------")
            
            if summ < goal :
                print("in summ < goal")
                print("summ:",summ)
                print("goal:",goal)
                print("------------------------------------")
                
                jumpper(p, nums_list, summ, step, goal)
            
            
            elif summ >= goal : #End  
                print("in summ >= goal")
                print(step)
                return step
          
                
        return jumpper(0, nums, 0, 1 , len(nums)-1)    
       
        #jumpper(0, nums, 2, 1 , nums[len(nums)-1])  #goal修 
      

s=Solution()
s.jump( [2,3,1,1,4])