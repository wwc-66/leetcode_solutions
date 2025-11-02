'''
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。





示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = "2"
输出：["a","b","c"]


提示：

1 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        diglet = {'2':'abc',
              '3':'def',
              '4':'ghi',
              '5':'jkl',
              '6':'mno',
              '7':'pqrs',
              '8':'tuv',
              '9':'wxyz'}
        #定义结果列表，用于储存结果
        result = []
        #定义递归函数
        def backtrack(output,nextDigit):
            #递归结束条件
            #当数字全部处理完
            if len(nextDigit) == 0:
                result.append(output)
            #否则
            else:
                #当前数字定义为第一个数字
                currentDigit = nextDigit[0]
                #数字对应字母
                letters = diglet[currentDigit]
                #遍历每个字母，与之前的output字母进行组合
                for letter in letters:
                    #对每个结果都进行递归调用
                    backtrack(output+letter,nextDigit[1:])
        #从初始开始递归
        backtrack('',digits)
        return result