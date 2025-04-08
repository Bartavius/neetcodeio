class Solution:
    def rotate(self, matrix) -> None:
        # reverse and transpose

        matrix.reverse()

        n = len(matrix) # n x n

        for i in range(n):
            for j in range(i + 1, n):
                # in lin alg, a12 -> a21 in transpose
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        