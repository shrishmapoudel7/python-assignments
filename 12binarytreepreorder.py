class BST:
    def __init__(self, key):    # self and key are box okay??  
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:    # node ma kei na vaye value yta huna paryo ni
            self.key = data     #aba chaina data rakha (that you have to put in binary tree node(BST))
            return

        if self.key == data:
            return

        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print("Node is found!")
            return

        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the tree!")
  # main 
                
    def preorder(self):
        print(self.key)     # self.key is 10
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
            

# Create the root node 


root = BST(10)                                           
# List of values to insert into the BST
list1 = [6, 3, 1, 6, 98, 3, 7]

# Insert values into the BST and print the preorder traversal
for i in list1:    #aba insert vo k turn wise turn
    root.insert(i)

root.preorder()






'''
  root =BST(10)
list1=[6,3,1,6,98,3,7]
for i on list1:
    root.inset(i)
root.preorder    (aba tyo value 6,3,1,2 haru sab preorder ma gako ie node ma)
  

note:
tyo c++ has obnject remember??
like aa.demo
     self.demo


     class demo           class BTS
     demo aa, self;          BTS KEY, SELF

'''


# in Python, we can directly create a BST object using binarytree module.
# bst() generates a random binary search tree and return its root node.