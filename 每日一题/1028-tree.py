class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == '-':
                level, i = level + 1, i + 1
            
            while i < len(S) and S[i] != '-':
                val, i = val + S[i], i + 1

            # to make sure the top node will always be
            # the parent node of potential child
            while len(stack) > level:
                stack.pop()

            node = TreeNode(val)

            if stack and stack[-1].left is None:
                stack[-1].left = node
            
            elif stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]