'''
202. 快乐数
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。



示例 1：

输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
示例 2：

输入：n = 2
输出：false


提示：

1 <= n <= 231 - 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        #创建一个集合，用于存储已经出现过的数字
        seen = set()
        #定义辅助函数，用于改变n值并计算各位置数字的平方和
        def get_next(num):
            total = 0
            #提取每一位数字，直到num归零
            while num != 0:
                digit = num % 10
                #取出当前位置的数字并计算平方
                total += digit ** 2
                num //= 10
            #返回total，得到最终平方和以及新的n
            return total
        #当n没有变成1且循环没有达到一整轮时
        while n != 1 and n not in seen:
            #集合中添加当前n
            seen.add(n)
            #更新n值
            n = get_next(n)
        return n == 1