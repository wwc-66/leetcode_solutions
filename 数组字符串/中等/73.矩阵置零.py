'''
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。



示例 1：


输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
示例 2：


输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]


提示：

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        #需要换0的行和列
        row_0 = [False] * m
        col_0 = [False] * n

        #计算并保存出现了0的行和列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_0[i] = True
                    col_0[j] = True

        #重新遍历矩阵，在需要换0的行/列上的元素赋值为0
        for x in range(m):
            for y in range(n):
                if row_0[x] or col_0[y]:
                    matrix[x][y] = 0