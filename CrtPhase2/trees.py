class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BST:
    def add_element(self,root,value):
        new_node=Node(value)
        if new_node.data<root.data:
            if root.left!=None:
                self.add_element(root.left,value)
            else:
                root.left=new_node
        else:
            if root.right != None:
                self.add_element(root.right, value)
            else:
                root.right = new_node
    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        print(root.data,end=' ')
        if root.right!=None:
            self.inorder(root.right)
    def preorder(self,root):
        print(root.data,end=' ')
        if root.left!=None:
            self.preorder(root.left)
        if root.right!=None:
            self.preorder(root.right)
    def postorder(self,root):
        if root.left!=None:
            self.postorder(root.left)
        if root.right!=None:
            self.postorder(root.right)
        print(root.data,end=' ')
    def levelorder(self,root):
        lst=[]
        lst.append(root)
        while len(lst)!=0:
            ele = lst.pop(0)
            print(ele.data,end=' ')
            if ele.left:
                lst.append(ele.left)
            if ele.right:
                lst.append(ele.right)
        if root.left==None and root.right==None:
            self.levelorder(root.left)
            self.levelorder(root.right)
    def treeHeight(self,root):
        if root==None:
            return -1
        leftHeight=self.treeHeight(root.left)
        rightHeight=self.treeHeight(root.right)
        return 1+max(leftHeight,rightHeight)
ob=BST()
root=Node(10)
ob.add_element(root,7)
ob.add_element(root,40)
ob.add_element(root,5)
ob.add_element(root,9)
ob.add_element(root,15)
ob.add_element(root,60)
ob.inorder(root)