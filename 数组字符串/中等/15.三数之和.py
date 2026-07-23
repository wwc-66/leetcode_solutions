'''
15. 三数之和
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #排序
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            #跳过重复元素（只有第一个正常运算，后续与之重复的元素均跳过）
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    #跳过左右指针移动时经过的重复元素
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    #左右指针移动到下一个非重复的新元素
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                elif s > target:
                    right -= 1
        return res