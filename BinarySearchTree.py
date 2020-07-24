class TraversalType:
  IN_ORDER = "inorder"
  PRE_ORDER = "preorder"
  POST_ORDER = "postorder"

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    if self.root == None:
      self.root = Node(data=data)
    else:
      self.insert_node(data, self.root)

  def insert_node(self, data, root):
    if data <= root.data:
      if root.left:
        self.insert_node(data, root.left)
      else:
        root.left = Node(data)
    else:
      if root.right:
        self.insert_node(data, root.right)
      else:
        root.right = Node(data)

  def display(self, traversal=TraversalType.IN_ORDER):
    print("Traversal Type: {}".format(traversal).center(30, "*"))
    if traversal == TraversalType.IN_ORDER:
      self.inorder(self.root)
    elif traversal == TraversalType.PRE_ORDER:
      self.pre_order(self.root)
    elif traversal == TraversalType.POST_ORDER:
      self.post_order(self.root)
    else:
      print("INVALID INPUT")


  def inorder(self, root):
    if root is None:
      return
    self.inorder(root.left)
    print("{} ".format(root.data))
    self.inorder(root.right)


  def pre_order(self, root):
    if root is None:
      return
    print("{} ".format(root.data))
    self.pre_order(root.left)
    self.pre_order(root.right)

  def post_order(self, root):
    if root is None:
      return
    self.post_order(root.left)
    self.post_order(root.right)
    print("{} ".format(root.data))


  def find(self, data):
    return self.find_node(self.root,data)

  def find_node(self, root, data):
    if(root is None):
      return False
    elif(data == root.data):
      return True
    elif(data < root.data):
      return self.find_node(root.left, data)
    else:
      return self.find_node(root.right, data)

  def findmin(self, root):
      if root is None:
          return None
      if root.left is None:
          return root
      return self.findmin(root.left)

  def delete(self, data):
      self.delete_node(self.root, data)

  def delete_node(self, root, data):
      if root is None:
          return None
      if data < root.data:
          root.left = self.delete_node(root.left, data)
      elif data > root.data:
          root.right= self.delete_node(root.right, data)
      else:
          if not root.left:
              return root.right
          elif not root.right:
              return root.left
          else:
              node = self.findmin(root.right)
              root.data = node.data
              root.right = self.delete_node(root.right, node.data)
      return root


if __name__=='__main__':
 ob = BinarySearchTree()
 ob.insert(20)
 ob.insert(9)
 ob.insert(40)
 ob.insert(8)
 ob.insert(11)
 ob.insert(33)
 ob.insert(44)
 ob.display(traversal=TraversalType.IN_ORDER)
 print("X".center(20, "*"))
 ob.delete(data=20)
 print("X".center(20, "*"))
 ob.display(traversal=TraversalType.IN_ORDER)

 # ob.display(traversal=TraversalType.PRE_ORDER)
 # print("X".center(20, "*"))
 # ob.display(traversal=TraversalType.POST_ORDER)
 # print("X".center(20, "*"))
 # data = 50
 # print("Find: {}".format(data))
 # print("{} --> Found {}".format(data,ob.find(data)))


