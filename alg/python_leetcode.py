#coding: utf-8



###### 动态规划算法 AC #################
class ac_303:

	def __init__(self, nums):
		self.nums = nums

	def sumRange(self, i ,j):
		return sum(self.nums[i: j+1]) if j < len(self.nums) else sum(self.nums[i:])


class ac_121:
    def maxProfit(self, prices):
        import sys
        max_profit, min_price = 0, sys.maxsize
        for per_price in prices:
            min_price = min(min_price, per_price)
            max_profit = max(max_profit, per_price-min_price)
        return max_profit

class ac_70_outTime:
    def climbStairs(self, n):
        """
           :type n: int
           :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class ac_70:
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n ==2:
            return 2
        first = 1
        second = 2
        for i in range(n-2):
            ret = first + second
            first = second
            second = ret
        return ret

class ac_53():
    def maxSubArray(self, nums):
        for index, values in enumerate(nums):
            if index == 0 :
                continue
            if nums[index-1] > 0:
                nums[index] += nums[index-1]
        return max(nums)


###### offer AC #################

# -*- coding:utf-8 -*-
class Solution_ac3:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        column_length = len(array[0]) #column 列       
        row_length = len(array) #row 行
        col, row = column_length - 1, 0
        while True:
            if col < 0 or row >= row_length:
                return False
            r_c_value = array[row][col]
            #print row,col,r_c_value
            if r_c_value == target:
                return True
            if array[row][col] > target:
                col -= 1
            if array[row][col] < target:
                row += 1

def test_offer3():
    ac_obj = Solution_ac3()
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print ac_obj.Find(16,array)
                            

if __name__ == '__main__':
    """
        ac_obj = ac_121()

        print(ac_obj.maxProfit([7,1,5,3,6,4]))
        ac_obj = ac_70(4)
    
    ac_obj = ac_70()
    print(ac_obj.climbStairs(4))
    """
    #ac_obj = ac_53()
    #print(ac_obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    test_offer3()
