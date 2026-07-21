'''
1. 两数之和
提示
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #定义存储字典，数为键，索引为值
        dic = {}
        #遍历给定数组
        for i in range(len(nums)):
            #查看当前数字与目标数之差是否已经被存储
            t = target - nums[i]
            #已经被存储，返回两数索引
            if t in dic:
                return [i,dic[t]]
            #没有，将当前数字存入
            else:
                dic[nums[i]] = i