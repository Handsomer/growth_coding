#coding = utf-8

###### 动态规划算法 AC #################
class ac_303:

	def __init__(self, nums):
		self.nums = nums

	def sumRange(self, i ,j):
		return sum(self.nums[i: j+1]) if j < len(self.nums) else sum(self.nums[i:])


if __name__ == '__main__':
	pass