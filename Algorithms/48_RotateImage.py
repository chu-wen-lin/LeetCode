class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # step 1. mirror the matrix
        # 1 4 7
        # 2 5 8
        # 3 6 9

        # step 2. reverse each row
        # 7 4 1
        # 8 5 2
        # 9 6 3

        n = len(matrix)

        if n == 1:
            return matrix

        for i in range(n):
            for j in range(i):  # 注意j的range是i!
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

        return matrix

        # what if counterclockwise?
        # swap matrix[i][j], matrix[n-j-1][n-i-1]
#         for i in range(n):
#             for j in range(n-i): # j的range是n-i
#                 matrix[i][j], matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1], matrix[i][j]

#         for row in matrix:
#             row.reverse()

#         return matrix
