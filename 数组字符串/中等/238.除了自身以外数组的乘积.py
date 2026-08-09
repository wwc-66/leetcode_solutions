'''
238. 除了自身以外数组的乘积
已解答
中等
相关标签
premium lock icon
相关企业
提示
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。



示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]


提示：

2 <= nums.length <= 105
-30 <= nums[i] <= 30
输入 保证 数组 answer[i] 在  32 位 整数范围内
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        forward = []
        backward = []
        #计算正向前缀积和逆向前缀积
        for fw in nums:
            if not forward:
                forward.append(fw)
            else:
                fw *= forward[-1]
                forward.append(fw)

        for bw in nums[::-1]:
            if not backward:
                backward.append(bw)
            else:
                bw *= backward[-1]
                backward.append(bw)
        backward.reverse()

        for i in range(len(nums)):
            if i == 0:
                ans = backward[1]
            elif i == len(nums) - 1:
                ans = forward[-2]
            else:
                ans = forward[i-1] * backward[i+1]
            answer.append(ans)
        return answer