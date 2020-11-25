#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if (start > end):
                return [
                    None,
                ]
            allTree = []
            for i in range(start, end + 1):
                leftTree = generateTrees(start, i - 1)
                rightTree = generateTrees(i + 1, end)
                for l in leftTree:
                    for r in rightTree:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTree.append(currTree)
            return allTree

        return generateTrees(1, n) if n else []


# @lc code=end
