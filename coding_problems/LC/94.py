# link:https://leetcode.com/problems/binary-tree-inorder-traversal/

# in order traversal, go down left subtree until it is a child node
# print it, then it goes back one level to that left subtree's root
# prints the root, then traverses right subtree
# if node == null: return
# inorder left_subtree
# visit node
# inorder right_subtree
from TreeNode import TreeNode
from typing import List


# we need this helper function in order to save the data that needs to be returned
# this helper function contains the bulk of the code and takes in an array as an additional arguement
# therefore, this is the function that is recursively called
def helper(root: TreeNode, storage_array) -> List[int]:
    
    if root == None:
        return
    # traverses the left subtree until we get to it's child node
    helper(root.left,storage_array)
    # once we find the child node, we store that node's value
    storage_array.append(root.val)
    # then we try the right subtree
    helper(root.right,storage_array)
    
def inorderTraversal(root: TreeNode) -> List[int]:
    values = []
    helper(root, values)
    return values
    

test_case_1 = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
test_case_2 = TreeNode(1)
# print(inorderTraversal(test_case_1))
print(inorderTraversal(test_case_1))

