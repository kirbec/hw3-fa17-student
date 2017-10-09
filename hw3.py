##################################
#                                #
#  Homework 3                    #
#  Released: September 26, 2017  #
#  Due: October 10, 2017         #
#                                #
##################################


# Matrix Transpose
#
# Description:
#     Given an m x n matrix A, return A^T, that is,
#     return the transpose of the matrix A.
#
# Example(s):
#
#     Example 1:
#         Input:
#             A = [[1]]
#         Output:
#             [[1]]
#
#     Example 2:
#         Input:
#             A = [[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]]
#         Output:
#             [[1, 4, 7],
#              [2, 5, 8],
#              [3, 6, 9]]
#
def matrix_transpose(A):
    newMatrix = [None]*len(A[0])
    for i in range(len(newMatrix)):
        newMatrix[i] = [None]*len(A)
    for r in range(len(A)):
        for c in range(len(A[0])):
            newMatrix[c][r] = A[r][c]
    print(newMatrix)
    return newMatrix



# Max Element in 2-D Array
#
# Description:
#     Given a 2-d array grid of integers,
#     determine the maximum number in grid.
#
# Example(s):
#     Example 1:
#         Input:
#             grid = [[4, 2],
#                     [3, -1]]
#         Output:
#             4
#
#     Example 2:
#         Input:
#             grid = [[-300, -200],
#                     [-300, -100]]
#         Output:
#             -100
#
def max_2d_array(grid):
    highest = grid[0][0]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (highest < grid[r][c]):
                highest = grid[r][c]
    return highest



# Binary Search
#
# Description:
#     Given a sorted (increasing) array with distinct integers and a
#     target integer, determine the index of target in the given array.
#     If target is not in the array, return None. Try to use the fact
#     that the array is sorted to optimize your algorithm.
#
# Example(s):
#
#     Example 1:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#             target = 3
#         Output:
#             2
#
#     Example 2:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#             target = 0
#         Output:
#             None
#
def binary_search(arr, target):
    lower = 0
    upper = len(arr) - 1
    while lower < upper:
        mid = int((upper-lower)/2) + lower
        print(lower,upper,mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lower = mid
        elif arr[mid] > target:
            upper = mid
    return None





# Sorted Matrix Search
#
# Description:
#     Given a square 2d array of integers and a target integer
#     return the coordinates of the target integer as a tuple
#     in the form (row, col) if the element exists in the matrix,
#     or None if the element does not exists. The 2d array
#     is guaranteed to be sorted ascending row-wise,
#     and the zeroth element of each row is strictly larger than
#     the last element of the previous row.
#
# Example(s):
#     Example 1:
#         Input:
#             arr = [[1 , 2 ,  3],
#                    [8 , 11, 16],
#                    [23, 24, 25]]
#             target = 8
#         Output:
#             (1, 0)
#
#     Example 2:
#         Input:
#             arr = [[1 , 2 ,  3],
#                    [8 , 11, 16],
#                    [23, 24, 25]]
#             target = 20
#         Output:
#             None
#
def search_2d_array(arr, target):
    row = arr[0]
    for r in range(len(arr)):
        if arr[r][0] > target:
            return binary_search(arr[r],target)
        elif arr[r][0] < target:
            row = arr[r]
        elif arr[r][0] == target:
            return ([r,0])
    return binary_search(arr[r],target)




# Maximum Sum Subarray
#
# Description:
#     Given an array of integers, determine the maximum sum of
#     a continuous subarray of the given array.
#
# Examples(s):
#     Example 1:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#         Ouput:
#             15
#
#     Example 2:
#         Input:
#             arr = [1, -3, 4, 1, -2, 3]
#         Output:
#             6
#
def max_sum_subarray(arr):
    pass



# Maximum Sum Sub-Rectangle
#
# Description:
#     Given a 2-d array of integers, determine the
#     maximum sub-rectangle sum.
#
# Example(s):
#     Example 1:
#         Input:
#             grid = [[1, 2],
#                     [3, 4]]
#         Output:
#             10
#
#     Example 2:
#         Input:
#             grid = [[1,  2],
#                     [-3, 0]]
#         Ouput:
#             3
#
#     Example 3:
#         Input:
#             grid = [[ 1, -2,  0],
#                     [-1,  3,  0],
#                     [ 3, -1, -9]]
#         Output:
#             4
#
def max_sum_subrectangle(grid):
    pass



# Maximum Number of Times an Array can be Flattened
#
# Description:
#     Given an array of integers and arrays,
#     return the maximum number of times arr can be flattened.
#     For example, if arr = [1, 2, [3, 4], 5],
#     then arr could be flattened once.
#
# Example(s):
#     Example 1:
#         Input:
#             arr = [1, 2, [3, 4], 5]
#         Output:
#             1
#
#     Example 2:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#         Output:
#             0
#
def max_array_flatten(arr):
    count = 0
    for i in range(len(arr)):
        print(type(arr[i]))
        if(type(arr[i]) != int):
            count += 1
    return count
