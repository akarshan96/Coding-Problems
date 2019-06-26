class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.level = None


class Tree:
    def __init__(self):
        self.root = None
        self.stack = []
        
    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if current.val < val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break

                elif current.val > val:
                    if current.right:
                            current = current.right
                    else:
                            current.right = Node(val)
                            break
                else:
                    break

                
    def inorder_traversal(self, node):
        if node == None:
            return -1
        else:
            self.inorder_traversal(node.left)
            print(node.val)
            self.inorder_traversal(node.right)
            
    def preorder_traversal(self, node):
        if node == None:
            return -1
        else:
            print(node.val)
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node == None:
            return -1
        else:
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)
            print(node.val)

    def get_root(self):
        return self.root

    def push(self,stack,val):
        stack.append(val)

    def pop(self,stack):
        if not stack:
            return -1
        else:
            return stack.pop(-1)

    def dfs(self):
        if not self.stack:
            return True
        else:
            current = self.pop(self.stack)
            print(current.val)
            if current.right:
                self.push(self.stack,current.right)
            if current.left:
                self.push(self.stack,current.left)
            self.dfs()

    def dfs_driver(self):
        self.push(self.stack,self.root)
        self.dfs()

    def depth(self, node):
        l = 0
        r = 0
        if self.root == None:
            return -1

        if node.left == None and node.right == None:
            return 0

        if node.left:
            l = 1 + self.depth(node.left)

        if node.right:
            r = 1 + self.depth(node.right)
        return max(l,r)
    

tree = Tree()
arr = [3,2,4,1,5]
for i in arr:
    tree.create(i)
#tree.inorder_traversal(tree.get_root())
#tree.preorder_traversal(tree.get_root())
#tree.postorder_traversal(tree.get_root())
#tree.dfs_driver()
print(tree.depth(tree.get_root()))
        
