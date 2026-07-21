'''
58. 最后一个单词的长度
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。



示例 1：

输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为 5。
示例 2：

输入：s = "   fly me   to   the moon  "
输出：4
解释：最后一个单词是“moon”，长度为 4。
示例 3：

输入：s = "luffy is still joyboy"
输出：6
解释：最后一个单词是长度为 6 的“joyboy”。


提示：

1 <= s.length <= 104
s 仅有英文字母和空格 ' ' 组成
s 中至少存在一个单词
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #初始化最后一个单词的变量
        word = ''
        #倒序循环给定字符串的每个字符
        for ch in s[::-1]:
            #如果检测到字母
            if ch.isalpha():
                word += ch
            #当检测到非字母时
            #1.最后一个单词后还有符号,跳过当前符号
            elif len(word) == 0 and not ch.isalpha():
                continue
            #2.已经获取到最后一个单词并且检测到非字母符号
            elif len(word) > 0 and not ch.isalpha():
                return len(word)
        return len(word)