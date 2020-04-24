from dll_stack import Stack
from dll_queue import Queue
from collections import deque

'''
import sys
sys.path.append('../queue_and_stack')
'''


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        while self:
            # print("self: " + str(self))
            # print("value: " + str(value))
            if value < self.value:
                if not self.left:
                    self.left = BinarySearchTree(value)
                    return
                else:
                    self = self.left
            else:
                if not self.right:
                    self.right = BinarySearchTree(value)
                    return
                else:
                    self = self.right

    def recursive_insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        # Return True if the tree contains the value
        # False if it does not
        while self:
            # print(self.value)
            # print(target)
            if target == self.value:
                return True
            elif target < self.value:
                if not self.left:
                    return False
                else:
                    self = self.left
            else:
                if not self.right:
                    return False
                else:
                    self = self.right

    # Return the maximum value found in the tree

    def get_max(self):
        # Initially set the max value to be self.
        max = self.value
        while self.right:
            if self.right.value > max:
                max = self.right.value
            self = self.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left and self.right:
            self.left.for_each(cb)
            self.right.for_each(cb)
        elif self.left:
            self.left.for_each(cb)
        elif self.right:
            self.right.for_each(cb)

    def for_each_lecture(self, cb):
        cb(self.value)
        # base case is when self has no left or right
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def for_each_iterative_depth_first(self, cb):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current_node = stack.pop()
            # Checking the right first will result in the same order as the
            # recursive (lecture) version above
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def for_each_iterative_breadth_first(self, cb):
        q = deque()
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            # for left to right ordering, check left first.
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # AKA Inorder Traversal
    # Recursively:
    #   1. Visit left subtree
    #   2. Visit node
    #   3. Visit right subtree

    def in_order_print(self, node):
        if node == None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        q = Queue()
        while node is not None:
            print(node.value)
            # Stick all of the node's children in the end of the queue.
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            if q.len() > 0:
                # Get the first node in the queue and continue the loop with it.
                node = q.dequeue()
            else:
                break
        return

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        s = Stack()
        while node is not None:
            print(node.value)
            # Stick all of the node's children in the end of the stack.
            if node.left:
                s.push(node.left)
            if node.right:
                s.push(node.right)
            if s.len() > 0:
                # Get the last node in the stack and continue the loop with it.
                node = s.pop()
            else:
                break
        return

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    '''
    To traverse a binary tree in preorder,
    1. Visit the root.
    2. Traverse the left sub tree of root.
    3. Traverse the right sub tree of root.
    '''

    def pre_order_dft(self, node):
        if node == None:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    '''
    To traverse a binary tree in postorder traversal,
    1. Traverse the left sub tree of root.
    2. Traverse the right sub tree of root.
    3. Visit the root.
    '''
    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if node == None:
            return

        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)


'''
my_bst = BinarySearchTree(1)
my_bst.insert(8)
my_bst.insert(5)
my_bst.insert(7)
my_bst.insert(6)
my_bst.insert(3)
my_bst.insert(4)
my_bst.insert(2)
# my_bst.bft_print(my_bst)
# my_bst.dft_print(my_bst)
# my_bst.pre_order_dft(my_bst)
my_bst.post_order_dft(my_bst)
'''
