class Solution:
    def sumRootToLeaf(self, root):

        def dfs(node, curr):
            if not node:
                return 0

            # update binary number
            curr = curr * 2 + node.val

            # leaf node check
            if node.left is None and node.right is None:
                return curr

            # explore children
            left_sum = dfs(node.left, curr)
            right_sum = dfs(node.right, curr)

            return left_sum + right_sum

        return dfs(root, 0)