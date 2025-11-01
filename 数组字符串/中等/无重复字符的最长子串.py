'''
3. 无重复字符的最长子串
提示
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 10 ** 4
s 由英文字母、数字、符号和空格组成
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s为空字符串，返回0
        if not s:
            return 0

        #用字典记录每个字符出现的位置
        char_index = {}
        #初始化左边界
        left = 0
        #初始化最长子串长度
        max_len = 0
        #遍历整个字符串
        for right in range(len(s)):
            #设置当前字符变量
            current_char = s[right]
            #如果当前字符已经在字典中，即已经在当前子串中
            if current_char in char_index and char_index[current_char] >= left:
                #左边界移动到旧字符的后一位，满足子串不重复的要求
                left = char_index[current_char] + 1

            #更新当前字符的位置。如果第一次出现，可用于后续检测的重复字符（上面一段代码的功能）
            char_index[current_char] = right

            #计算当前子串长度
            current_len = right - left + 1
            #如果当前子串比最大子串长度大，更新最大长度
            if current_len > max_len:
                max_len = current_len

        return max_len