class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []: return []

        res = []
        up = 0
        left = 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1

        direction = 0 # 0 to right, 1 to down, 2 to left, 3 to up

        while True:

            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1

            if direction == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1

            if direction == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1

            if direction == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1

            if left > right or up > down: return res
            direction = (direction + 1) %4
