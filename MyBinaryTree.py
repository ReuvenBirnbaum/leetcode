from typing import List
import unittest

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

         
class Solution:
    def preorderTraversalRec(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        result = [root.val]
        result.extend(Solution().preorderTraversalRec(root.left))
        result.extend(Solution().preorderTraversalRec(root.right))
        return result

    def preorderTraversal(self, root:TreeNode) -> List[int]:
        if root ==None:
            return []
        history = [[root,0]]
        result = [root.val]
        while not history==[]:
            if history[-1][1]==0:
                history[-1][1]=1
                if not history[-1][0].left==None:
                    history.append([history[-1][0].left,0])
                    result.append(history[-1][0].val)
            elif history[-1][1]==1:
                history[-1][1]=2
                if not history[-1][0].right == None:
                    history.append([history[-1][0].right,0])
                    result.append(history[-1][0].val)
            elif history[-1][1]==2:
                history.pop()
        return result
                
                
            

class MyBinaryTreeTestCase(unittest.TestCase):

    def testpreorderTraversalRec(self):
        preorderTraversal = Solution().preorderTraversalRec
        myTree = TreeNode(0)
        myTree.left = TreeNode(1)
        myTree.left.right = TreeNode(2)
        myTree.right = TreeNode(3)
        myTree.right.left = TreeNode(4)
        self.assertEqual([0,1,2,3,4],preorderTraversal(myTree))

        
    def testpreorderTraversalIte(self):
        preorderTraversal = Solution().preorderTraversal
        myTree = TreeNode(0)
        myTree.left = TreeNode(1)
        myTree.left.right = TreeNode(2)
        myTree.right = TreeNode(3)
        myTree.right.left = TreeNode(4)
        self.assertEqual([0,1,2,3,4],preorderTraversal(myTree))


 
if __name__ == '__main__':
    unittest.main()
