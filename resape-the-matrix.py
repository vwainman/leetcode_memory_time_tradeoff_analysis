# https://leetcode.com/problems/reshape-the-matrix/description/
#
# In MATLAB, there is a handy function called reshape which can reshape an m x
# n matrix into a new one with a different size r x c keeping its original
# data.
#
# You are given an m x n matrix mat and two integers r and c representing the
# number of rows and the number of columns of the wanted reshaped matrix.
#
# The reshaped matrix should be filled with all the elements of the original
# matrix in the same row-traversing order as they were.
#
# If the reshape operation with given parameters is possible and legal, output
# the new reshaped matrix; Otherwise, output the original matrix.


from typing import List


def matrix_reshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    n_items = 0
    mat_row_len = len(mat[0])
    n_items += len(mat[0]) * len(mat)

    if n_items != r * c:
        return mat

    i, j = 0, 0
    new_mat = []

    for _ in range(r):
        new_mat_row = []
        for _ in range(c):
            if j == mat_row_len:
                j = 0
                i += 1
            new_mat_row.append(mat[i][j])
            j += 1
        new_mat.append(new_mat_row)
    return new_mat
