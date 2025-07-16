"""
Task: Find the area of the largest square containing only 1's in a 2D binary matrix.
You are given a 2D binary matrix filled with 0's and 1's. Your goal is to find the largest square containing only 1's and return its area.

Example:
matrix = [
    "01101",
    "11110",
    "01110",
    "11110",
    "11011",
    "00000"
]
Output: 9  # The largest square has a size of 3x3, so area = 9

==== First Thoughts – Brute Force Approach:
My first idea is to check every possible square submatrix and see if it contains only 1’s:
--- Start at each cell.
--- Try to expand a square as long as all values inside it are '1'.
--- Track the maximum size.

However:
This involves four nested loops:
Two to pick the top-left corner of the square, and two more to verify all elements inside the square.
Time complexity: O(n^4) in the worst case.
Not scalable for large matrices.

Sooo... we can search for a better way to do that.
Instead of repeatedly checking each square, we can break the problem into smaller subproblems using DP with time complexity of O(m * n) or O(n**2) for square matrix
"""


def max_square_area(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side


matrix = [
    "01101",
    "11110",
    "01110",
    "11110",
    "11011",
    "00000"
]

matrix = [list(row) for row in matrix]
print(max_square_area(matrix))
