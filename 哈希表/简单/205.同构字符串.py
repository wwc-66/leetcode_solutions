'''
205. 同构字符串
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。



示例 1:

输入：s = "egg", t = "add"
输出：true
示例 2：

输入：s = "foo", t = "bar"
输出：false
示例 3：

输入：s = "paper", t = "title"
输出：true


提示：

1 <= s.length <= 5 * 104
t.length == s.length
s 和 t 由任意有效的 ASCII 字符组成
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_1st = {}
            l_s = []
            t_1st = {}
            l_t = []
            for i, sc in enumerate(s):
                if sc not in s_1st:
                    s_1st[sc] = i
                    l_s.append(i)
                else:
                    l_s.append(s_1st[sc])

            for j, tc in enumerate(t):
                if tc not in t_1st:
                    t_1st[tc] = j
                    l_t.append(j)
                else:
                    l_t.append(t_1st[tc])

            return l_s == l_t