'''
14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 如果非空，则仅由小写英文字母组成
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 如果是空列表，返回空字符串
        if not strs:
            return ''

        # 找到最短单词
        shortest_word = min(strs, key=len)

        # 遍历最短单词的每一个字母，与其他单词的同位置字母相比对
        for i in range(len(shortest_word)):
            current_letter = shortest_word[i]

            for word in strs:
                if word[i] != current_letter:
                    return shortest_word[:i]

        return shortest_word