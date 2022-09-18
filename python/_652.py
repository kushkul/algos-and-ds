# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def _hash(x):
            from hashlib import sha256
            S = sha256()
            S.update(x.encode())
            return S.hexdigest()

        def merkel(node):
            if not node:
                return '#'
            l_merkel = merkel(node.left)
            r_merkel = merkel(node.right)
            node.merkel = _hash(l_merkel + str(node.val) + r_merkel)
            subtree_map[node.merkel].append(node)
            return node.merkel

        from collections import defaultdict
        subtree_map = defaultdict(list)
        merkel(root)
        return [nodes.pop() for nodes in subtree_map.values() if len(nodes) >= 2]
            
