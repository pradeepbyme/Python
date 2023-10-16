# Dimension : The number of indices or subscripts
# needed to access an element within a multidimensional array
# is called its dimension.
# For example, a 2D array has two dimensions: row and column.

# 1 - D Array
array1 = [1]
# 2 - D Array
array2 = [[1, 2, 3], [4, 5, 6]]
# 3 - D Array
array3 = [[[1, 2, 3],
           [4, 5, 6],
           ]]



for i in range(0, 2):
    print(array3[0][i][1])
