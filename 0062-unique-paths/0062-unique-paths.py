class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        arr = []
        initial_col = [0] * (n-1)
        initial_col.append(1)

        last_col = [1] * n

        #initial array
        for row in range(m-1):
            arr.append(initial_col)   
        arr.append(last_col)

        for row in range(m-2,-1,-1):
            for col in range(n-2,-1,-1):
                arr[row][col] = arr[row+1][col] + arr[row][col+1]

        return arr[0][0]
        
        
        