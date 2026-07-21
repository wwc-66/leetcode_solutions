'''
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
示例 3：

输入：nums = [1,0,1,2]
输出：3
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 集合去重，定义最长连续序列长度变量及初始值
        num_set = set(nums)
        max_len = 0

        # 遍历集合中的数字，筛选序列首元素
        for num in num_set:
            if num - 1 not in num_set:
                # 定义当前数字值和当前连续序列长度
                current = num
                current_len = 1

                # 计算当前连续序列长度并对比更新max_len
                while current + 1 in num_set:
                    current += 1
                    current_len += 1

                max_len = max(max_len, current_len)

        return max_len