'''Task: Transpose a Matrix
Description:
Write a Python program that transposes a 2D matrix using two different methods:
  Using nested loops
  Using a list comprehension
Then, print the resulting transposed matrix.'''


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transposed.append(row)

print("Transposed matrix:")
for row in transposed:
    print(row)

transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("\nTransposed matrix:")
for row in transposed:
    print(row)
