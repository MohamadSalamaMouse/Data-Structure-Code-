class tree:
    def __init__(self,root):
        self.key=root
        self.left_child=None
        self.right_child=None
    def insert_left(self,new_node):
        if self.left_child==None:
            self.left_child=tree(new_node)
        else:
            t=tree(new_node)
            t.left_child=self.left_child
            self.left_child=t
    def insert_right(self,new_node):
        if self.right_child==None:
            self.right_child=tree(new_node)
        else:
            t=tree(new_node)
            t.right_child=self.right_child
            self.right_child=t
    
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def set_root_val(self,obj):
        self.key=obj
    def get_root_val(self):
        return self.key
    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
    def inorder(self):
        
        if self.left_child:
            self.left_child.preorder()
        print(self.key)
        if self.right_child:
            self.right_child.preorder()
    def postorder(self):
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
        print(self.key)
root=tree("a")
print("print root value :",root.get_root_val())
print("left child :",root.get_left_child())
print("right child :",root.get_right_child())
root.insert_left("b")
print("left child :",root.get_left_child())
print("left child sub tree :",root.get_left_child().get_root_val())
root.insert_right("hello")
print("right child :",root.get_right_child())
print("left child sub tree :",root.get_right_child().get_root_val())
root.preorder()
print("===========")
root.inorder()
print("========")
root.postorder()