class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1

        while l <= r and t <= b:

            # top row
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1

            # right column
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1

            # bottom row
            if t <= b:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1

            # left column
            if l <= r:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1

        return res