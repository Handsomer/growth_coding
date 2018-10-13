#coding = utf-8

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


if __name__ == '__main__':
    """
        ac_obj = ac_121()

        print(ac_obj.maxProfit([7,1,5,3,6,4]))
        ac_obj = ac_70(4)
    """
    ac_obj = ac_70()
    print(ac_obj.climbStairs(4))
