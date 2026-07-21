'''
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的 回文 子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
'''

'''
动态规划做法：
'''

def longestPalindrome(self, s: str) -> str:
    n = len(s)
    max_len = 1
    max_s = s[0]
    # 创建一个 n 行 n 列的二维列表，所有值初始化为 False
    dp = [[False] * n for _ in range(n)]
    for L in range(2, n+1):
        i = 0
        j = L - 1
        while j <= n-1:
            #检验首尾字符是否相等
            #首尾字符相等，且当前字符串长度L小于等于3，或L大于3但dp[i+1][j-1]值为True时，令dp[i][j]为True
            #即确认为回文子串
            if s[i] == s[j] and (L <= 3 or dp[i+1][j-1]):
                dp[i][j] = True
                #更新最长回文子串长度
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_s = s[i:j+1]
            #窗口后移
            i += 1
            j += 1

    return max_s

'''
在Python中，“中心扩展法”比动态规划更快
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        def expand(left: int, right: int) -> str:
            # 向外扩展，直到不满足回文条件
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # 退出循环时，s[left+1 : right] 是有效的回文子串
            return s[left + 1:right]

        res = s[0]
        for i in range(n):
            # 1. 奇数长度回文（中心是一个字符）
            odd = expand(i, i)
            # 2. 偶数长度回文（中心是两个字符之间）
            even = expand(i, i + 1)

            # 保留最长的
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res