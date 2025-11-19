'''
20. 有效的括号
提示
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
3.每个右括号都有一个对应的相同类型的左括号。


示例 1：

输入：s = "()"

输出：true

示例 2：

输入：s = "()[]{}"

输出：true

示例 3：

输入：s = "(]"

输出：false

示例 4：

输入：s = "([])"

输出：true

示例 5：

输入：s = "([)]"

输出：false



提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
'''

class Solution:
    def isValid(self, s: str) -> bool:
        match_table = {')':'(',']':'[','}':'{'}
        stack = []

        for ch in s:
            #当前字符为左括号
            if ch in match_table.values():
                #括号压入栈内
                stack.append(ch)
            #当前字符为右括号
            elif ch in match_table:
                #栈为空但遇上右括号
                if not stack:
                    return False
                #栈顶括号与当前右括号匹配
                if stack[-1] == match_table[ch]:
                    stack.pop()
                #括号类型不匹配
                else:
                    return False
        #栈为空，则完成匹配
        return True if not stack else False