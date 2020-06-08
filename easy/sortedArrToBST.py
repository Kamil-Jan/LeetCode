from typing import List
import time
import random


class TreeNode:
    def __init__(self, val=None, height=1):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = height

    def __str__(self):
        string = f"Tree node: val={self.val}, height={self.height}"
        return string


class AVL_Tree:
    def __init__(self, root):
        self.root = TreeNode(val=root)

    def insert(self, number):
        """
        Inserts a given number into a Tree.
        """
        node = self._insert(number)
        self._update_heights(node)
        while abs(self._get_bf(node)) <= 1:
            if not node.parent:
                break
            node = node.parent
        self.__balance(node)

    def _insert(self, number):
        """
        Inserts a given number into a Tree.

        Check the root of the tree. If the number
        is greater than the root, we look at the right subtree.
        If less - left. Repeat the operation until the number falls
        into place of the leaf.
        """
        node = self.root
        while True:
            # Check if a number is greater than node.
            if number >= node.val:
                # Check if a node.right is None
                if not node.right:
                    # node.right is a leaf
                    node.right = TreeNode(val=number)
                    node.right.parent = node
                    # node.height = self._get_height(node)
                    return node
                node = node.right
            else:
                # Check if a node.left is None
                if not node.left:
                    # node.left is a leaf
                    node.left = TreeNode(val=number)
                    node.left.parent = node
                    # node.height = self._get_height(node)
                    return node
                node = node.left

    def _get_height(self, node):
        """
        Returns node's height
        """
        if not node:
            return 0
        return node.height

    def _set_height(self, node):
        """
        Counts height of a given node.
        """
        if node.left == None or node.right == None:
            if node.left == node.right:
                return 1
            if node.left and not node.right:
                return node.left.height + 1
            if not node.left and node.right:
                return node.right.height + 1
        return max(node.left.height, node.right.height) + 1

    def _update_heights(self, node):
        """
        Updates heights of Tree's nodes.
        """
        while node:
            new_height = self._set_height(node)
            node.height = new_height
            node = node.parent

    def _get_bf(self, node):
        """
        Counts __balance factor of a given node.
        """
        return self._get_height(node.left) - self._get_height(node.right)

    def __balance(self, node):
        """
        Decides how subtree should be rotated.
        """
        if self._get_bf(node) == 2: # Left-heavy
            if self._get_bf(node.left) == 1:
                self.__LL_rotate(node) # Left-Left heavy
            else: # Left-Right heavy
                self.__LR_rotate(node)
        elif self._get_bf(node) == -2: # Right-heavy
            if self._get_bf(node.right) == -1: # Right-Right heavy
                self.__RR_rotate(node)
            else: # Right-Left heavy
                self.__RL_rotate(node)

    def __LL_rotate(self, node):
        """
        Left-Left rotation.

            A       B
          B   ==> C   A
        C
        """
        A = node
        B = A.left
        if A == self.root:
            self.root = B
        elif A.parent.left == A:
            A.parent.left = B
        else:
            A.parent.right = B

        A.left, B.right = B.right, A

        # Update parents
        B.parent, A.parent = A.parent, B
        self._update_heights(A)

    def __RR_rotate(self, node):
        """
        Right-Right rotation.

        A           B
          B   ==> A   C
            C
        """
        A = node
        B = A.right
        if A == self.root:
            self.root = B
        elif A.parent.left == A:
            A.parent.left = B
        else:
            A.parent.right = B
        A.right, B.left = B.left, A

        # Update parents
        B.parent, A.parent = A.parent, B
        self._update_heights(A)

    def __LR_rotate(self, node):
        """
        Left-Right rotation.

          A         A       C
        B    ==>  C   ==> B   A
          C     B
        """
        A = node
        B = A.left
        self.__RR_rotate(B)
        self.__LL_rotate(A)

    def __RL_rotate(self, node):
        """
        Right-Left rotation.

        A        A           C
          B  ==>   C   ==> A   B
        C            B
        """
        A = node
        B = A.right
        self.__LL_rotate(B)
        self.__RR_rotate(A)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        mid = len(nums) // 2
        mediana = nums[mid]
        t = AVL_Tree(mediana)
        if mid > 0:
            for num in nums[mid - 1::-1]:
                t.insert(num)
            for num in nums[mid + 1:]:
                t.insert(num)
        return t.root

