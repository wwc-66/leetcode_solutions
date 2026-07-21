'''
121. 买卖股票的最佳时机
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。



示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。


提示：

1 <= prices.length <= 10**5
0 <= prices[i] <= 10**4
'''

'''以下为个人解法，可以实现功能，但当输入的prices列表过大时，效率不足'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #初始化利润列表，初始元素为0，用于无法赚取利润时返回
        profit = [0]
        #遍历每购入价格索引，代表购入时为第i天
        for i in range(len(prices)-1):
            #定义可卖出价格列表
            sale = prices[i:]
            #计算最大利润
            p = max(sale) - prices[i]
            profit.append(p)
        #返回最高利润
        return max(profit)

'''以下为题解区参考代码'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0 # 边界条件
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]

'''
解析如下：
1.minprice最低价初始化为prices列表的第一位元素

2.遍历prices列表
  更新minprice的值，取最小使minprice总是最低

3.dp列表则为利润列表，取前一天利润与当天卖出利润的较大值
  即如果当天利润较低，则当天利润记录为前一天利润

妙处所在：
1.遍历prices列表时，仅对当前天数的数据改动，因此总是能保证卖出能在购入之后
2.利润列表dp采取当前天数利润为max（前一天利润，今天利润-购入价格）的计算方法，
  即，即使得到最大利润后，其后续每一天利润都在下降，
  将后续每天的利润都记作之前最大的利润，
  在最终返回时只需返回最后一位即可，效率非常高
'''

'''
还有更加高效简洁的解法如下
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #初始化利润为0
        profit = 0
        #最小购入价格取prices列表的第一个元素即第一天价格
        min = prices[0]
        #遍历prices列表
        for price in prices:
            #如果当天卖出- 最小购入价格即当天利润大于profit即之前最大利润
            if price - min >profit:
                #更新最大利润
                profit = price - min
            #如果当天价格比最小购入价格还要低
            if price < min:
                #更新最小购入价格
                min = price
        return profit

'''
妙处所在：
1.只用一个变量记录利润，而不是像之前用列表，高效很多
2.只遍历了一次，这也是拉开效率差距的最核心原因
'''