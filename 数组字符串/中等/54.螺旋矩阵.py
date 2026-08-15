'''
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。



示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            # 向右
            for r in range(left, right + 1):
                res.append(matrix[top][r])
            top += 1
            # 向下
            for d in range(top, bottom + 1):
                res.append(matrix[d][right])
            right -= 1
            # 向左
            if top <= bottom:
                for l in range(right, left - 1, -1):
                    print(l)
                    res.append(matrix[bottom][l])
                bottom -= 1
            # 向上
            if left <= right:
                for u in range(bottom, top - 1, -1):
                    print(u)
                    res.append(matrix[u][left])
                left += 1

        return res