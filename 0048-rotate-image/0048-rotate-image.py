class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        N = len(matrix)
        if N == 1: return

        # 행을 중심으로 뒤집기
        l, r = 0, N-1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        # 대각선을 중심으로 뒤집기
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]





