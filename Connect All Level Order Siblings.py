from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  #corner case
  if root is None:
    return root

  q = [root]
  prev = None
  while q:
    lvl_size = len(q)
    for _ in range(lvl_size):
      node = q.pop(0)

      #if node not root
      if prev:
        prev.next = node
      prev = node

      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
        
  return root


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()
