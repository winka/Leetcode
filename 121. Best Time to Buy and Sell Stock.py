# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 14:20:47 2022

@author: user
#   best
class Solution(object):
    def maxProfit(self, prices):  # acts as an unbounded upper value for comparison. 
                                  # This is useful for finding lowest values for something.
        min_price = float('inf') #用於幫忙尋找最小的路徑的用法(先不付值,傳到路徑中變成最小的數?)
        maybe_best_profit = 0
        best_profit = 0 
        
        
        for price in prices:
            min_price = min(min_price, price)
            maybe_best_profit = price - min_price
            best_profit = max(best_profit ,maybe_best_profit)
            
            
        return(best_profit)

s = Solution()
s.maxProfit([7,1,5,3,6,4])


'''
#   What is the point of float('inf') in Python?
https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
'''
"""
class Solution(object):
    def maxProfit(self, prices):
        dic ={}
        
        for index, value in enumerate(prices) :
            
            for  i in  range(index): 
                price_count = prices[index] - prices[i]

                
                if price_count > 0: 
                    print("index:",index,"price:",price_count)
                    dic[price_count] = index
       
        if not dic: 
            return 0
        else:    
            return (max(dic.keys()))
         
s = Solution()
s.maxProfit([7,6,4,3,1])
            
        
