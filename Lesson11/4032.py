#  ماتریس‌ها با استفاده از لیست‌های پایتون :
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
]
elment = matrix[1][2]
print("Elment at [1][2]:", elment)
print("Matrix elment:")
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()

# ماتریس‌ها با استفاده از کتابخانه‌ی NumPy :
import numpy  as np
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
elment = matrix[1,2]
print("Elment at [1,2]", elment)
matrix2 = np.array([
    [9,8,7],
    [6,5,4],
    [3,2,1]
])
result = matrix + matrix2
print("sum of matrices")
print(result)
