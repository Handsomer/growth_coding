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


if __name__ == '__main__':
    ac_obj = ac_121()

    print(ac_obj.maxProfit([7,1,5,3,6,4]))
