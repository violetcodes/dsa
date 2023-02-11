
class BSTNode:
    def __init__(self, item):
        self.item = item 
        self.parent = None 
        self.left = None 
        self.right = None 
        self.height = 0

    def insert(self, node):
        if node < self:
            self.insert_on_left(node)
            self.height = max(self.left.height + 1, self.height)
            
        else:
            self.insert_on_right(node) 
            self.height = max(self.right.height + 1, self.height)
        
        
    def skew(self): 
        hr = self.right.height if self.right is not None else -1
        hl = self.left.height if self.left is not None else -1
        return hr - hl 

    def insert_on_left(self, node):
        if self.left is None:
            self.left = node 
            node.parent = self 
        else:
            self.left.insert(node)
    
    def insert_on_right(self, node):
        if self.right is None:
            self.right = node 
            node.parent = self 
        else:
            self.right.insert(node)

    def __gt__(self, node):
        return self.item > node.item 
    
    def __eq__(self, node):
        return self.item == node.item 

    def __lt__(self, node):
        return self.item < node.item 

    @staticmethod
    def inorder_traversal(node):
        if node is None:
            return []
        return BSTNode.inorder_traversal(node.left) + [node.item,] + BSTNode.inorder_traversal(node.right)    
            
    @staticmethod
    def top_down_traversal(node):
        levels = {}
        queue = [node, ]

        while queue:
            q = queue.pop(0)
            
            if q.height in levels:
                levels[q.height].append(q.item)
            else:
                levels[q.height] = [q.item,]
            if q.left is not None:
                queue.append(q.left)
            if q.right is not None:
                queue.append(q.right)
            
        return levels 

    def __str__(self,):
        a = ''
        if self.left is not None:
            a += f'l:{self.left.item}'
        a += f'-({self.item, self.height})-'
        if self.right is not None:
            a += f'r:{self.right.item}'
        return a 




class BST:
    def __init__(self, node=None):
        self.root = node

    def insert(self, node):
        if not isinstance(node, BSTNode):
            node = BSTNode(node)
        if self.root is None:
            self.root = node 
        else:
            self.root.insert(node)

            
def build_balanced(arr):
    # arr = sorted(arr)

    root_bst = BST()

    if len(arr) == 0:
        return root_bst

    n = len(arr)
    root_bst.insert(arr[n//2])
    
    left_node = build_balanced(arr[:n//2]).root
    right_node = build_balanced(arr[n//2+1:]).root
    

    if left_node is not None:
        root_bst.root.insert(left_node)
    if right_node is not None:
        root_bst.root.insert(right_node)
    return root_bst

def is_balanced(node):
    if node is None:
        return True 
    return is_balanced(node.left) and (node.skew() in [0, 1, -1]) and is_balanced(node.right)


def test_bstnode():
    import random 
    to_add = [random.randint(0, 20) for _ in range(20)]
    print(to_add)
    bst = BST()
    for x in to_add:
        bst.insert(x)
        # print(bst.root.height, 'after', x)

    print('inorder:')
    print(bst.root.height, bst.root.skew())
    print(BSTNode.inorder_traversal(bst.root))
    

    # bst2 = BST()
    to_add = sorted(to_add)
    bst2 = build_balanced(to_add)
    print(bst2.root.height, bst2.root.skew())
    print('inorder2:')
    print(BSTNode.inorder_traversal(bst2.root))
    print(BSTNode.top_down_traversal(bst2.root))
    






test_bstnode()
            

