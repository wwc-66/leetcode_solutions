'''
3121. 统计特殊字母的数量 II
提示
给你一个字符串 word。如果 word 中同时出现某个字母 c 的小写形式和大写形式，并且 每个 小写形式的 c 都出现在第一个大写形式的 c 之前，则称字母 c 是一个 特殊字母 。

返回 word 中 特殊字母 的数量。



示例 1:

输入：word = "aaAbcBC"

输出：3

解释：

特殊字母是 'a'、'b' 和 'c'。

示例 2:

输入：word = "abc"

输出：0

解释：

word 中不存在特殊字母。

示例 3:

输入：word = "AbBCab"

输出：0

解释：

word 中不存在特殊字母。



提示：

1 <= word.length <= 2 * 105
word 仅由小写和大写英文字母组成。
'''

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        letters = ['a','b','c','d',
                   'e','f','g','h',
                   'i','j','k','l',
                   'm','n','o','p',
                   'q','r','s','t',
                   'u','v','w','x',
                   'y','z']
        lower = {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1,
                 'g': -1, 'h': -1, 'i': -1, 'j': -1, 'k': -1, 'l': -1,
                 'm': -1, 'n': -1, 'o': -1, 'p': -1, 'q': -1, 'r': -1,
                 's': -1, 't': -1, 'u': -1, 'v': -1, 'w': -1, 'x': -1,
                 'y': -1, 'z': -1}
        upper = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1,
                 'F': -1, 'G': -1, 'H': -1, 'I': -1, 'J': -1,
                 'K': -1, 'L': -1, 'M': -1, 'N': -1, 'O': -1,
                 'P': -1, 'Q': -1, 'R': -1, 'S': -1, 'T': -1,
                 'U': -1, 'V': -1, 'W': -1, 'X': -1, 'Y': -1,
                 'Z': -1}
        #for循环遍历word中每个字母及其索引
        for pos, char in enumerate(word):
            #如果是小写字母，则时刻更新其最新位置，直到最后一次出现
            if char in lower:
                lower[char] = pos
            #如果是大写字母，只记录第一次出现的位置
            elif char in upper and upper[char] == -1:
                upper[char] = pos

        #遍历每个字母，获取其大小写的索引并比较
        for letter in letters:
            #当二者均不为0且大写字母的第一次出现位置比小写字母的最后一次出现位置更大的时候，count+1
            if lower[letter] != -1 and upper[letter.upper()] != -1 and lower[letter] < upper[letter.upper()]:
                count += 1
        return count