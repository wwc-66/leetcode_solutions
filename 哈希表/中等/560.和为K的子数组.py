'''
560. 和为 K 的子数组
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。



示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2


提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        s = {0:1}
        current_num = 0
        for n in nums:
            current_num += n
            if current_num - k in s:
                res += s[current_num - k]
            if current_num in s:
                s[current_num] += 1
            else:
                s[current_num] = 1

        return res