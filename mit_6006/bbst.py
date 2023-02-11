

class BSTNode:
    @staticmethod
    def height_fn(node):
        if node is None:
            return -1
        return max(
            BSTNode.height_fn(node.left), 
            BSTNode.height_fn(node.right)) + 1

    def __init__(self, item):
        self.item = item 
        self.left = None 
        self.right = None
        self.parent = None 

    @property
    def height(self, ):
        return BSTNode.height_fn(self)

    @property
    def skew(self, ):
        return BSTNode.height_fn(self.right) - BSTNode.height_fn(self.left)

    def _left_most_child(self, ):
        if self.left is None: return self 
        return self.left._left_most_child()
    
    def _right_most_child(self, ):
        if self.right is None: return self 
        return self.right._right_most_child()

    def _first_left_ancestor(self, ):
        parent = self.parent 
        if parent is None:
            return None 
        if parent.left == self:
            return parent
        return parent._first_left_ancestor()

    def _first_right_ancestor(self, ):
        parent = self.parent 
        if parent is None:
            return None 
        if parent.right == self:
            return parent
        return parent._first_right_ancestor()


    def find_next(self, ):
        if self.right is not None:
            return self.right._left_most_child()
        return self._first_left_ancestor()

    def find_prev(self, ):
        if self.left is not None:
            return self.left._right_most_child()
        return self._first_right_ancestor() 

    def insert_next(self, node):
        if self.right is None:
            self.right = node 
            node.parent = self 
            return 

        left_most_child = self.right._left_most_child()
        left_most_child.left = node 
        node.parent = left_most_child 

        # left_most_child._balance() 
        # self._maintain() 

    def insert_prev(self, node):  # O(logH)
        if self.left is None:
            self.left = node 
            node.parent = self 
            return 
        
        right_most_child = self.left._right_most_child()
        right_most_child.right = node 
        node.parent = right_most_child

        # left_most_child._balance() 
        # self._maintain()

    def insert_node(self, node):
        if node.item < self.item:
            if self.left is None:
                self.left = node 
                node.parent = self 
            else:
                self.left.insert_node(node)
        elif node.item > self.item:
            if self.right is None:
                self.right = node 
                node.parent = self 
            else:
                self.right.insert_node(node)
            
        else:
            if self.left is None:
                self.left = node 
                node.parent = self 
            elif self.right is None:
                self.right = node 
                node.parent = self 
            else:
                self.left.insert_node(node)


    @property
    def _is_leaf(self, ):
        return (self.left is None) and (self.right is None)

    def _swap(self, node):
        self.item, node.item = node.item, self.item 

    def remove_node(self, ):  # O(logH)
        if self._is_leaf:
            p = self.parent
            if p.left is self: p.left = None 
            else: p.right = None 
            del self 
            return 
        
        if self.left is not None:
            prev_node = self.find_prev()
            prev_node._swap(self)
            prev_node.remove_node()
            return 
        
        else:
            next_node = self.find_next()
            next_node._swap(self)
            next_node.remove_node() 
    
    def rotate_left(self, ): # O(1)
        right = self.right 
        if right is None:
            return
        right_left = right.left
        parent = self.parent  
        
        self.right = right_left
        if right_left is not None:
            self.right.parent = self

        right.left = self
        self.parent = right 

        if parent is not None:
            if parent.left == self: parent.left = right 
            else: parent.right = right 
        right.parent = parent 

    def rotate_right(self, ):  # O(1)
        left = self.left
        if left is None:
            return 
        left_right = self.left.right
        parent = self.parent 

        self.left = left_right
        if left_right is not None:
            left_right.parent = self 

        left.right = self 
        self.parent = left 

        if parent is not None:
            if parent.left is self: parent.left = left 
            else: parent.right = left 


    def _is_balanced(self, ):
        return (
            (self._skew in (-1, 0, 1)) 
            and ((self.left is None) or self.left._is_balanced()) 
            and ((self.right is None) or self.right._is_balanced())
        )

    
    
    def _show(self, ): # Not tested
        backslash_char = '\\'
        a = '' if self.parent is None else str({self.parent.item})
        a = f"{a:^20}" + '\n'
        a + f"{'|':^20}" + '\n'
        a += f"{str(self.item):^20}" + '\n'
        a += f"{'/':^10}" + f"{backslash_char:^10}" + '\n'
        l, r = map(lambda k: ('' if k is None else str(k.item)), [self.left, self.right])
        a += f"{l:^10}" + f"{r:^10}"
        return a 

    
    @staticmethod
    def _from_arr(arr):
        n = len(arr)
        if n == 0:
            return 

        # print('n: arr:', n, arr)
        middle_item = arr[n//2]
        node = BSTNode(middle_item)

        if n == 1:
            return node
        
        left_node = BSTNode._from_arr(arr[:n//2])
        right_node = BSTNode._from_arr(arr[n//2+1:])
        node.left = left_node
        node.right = right_node
        if left_node is not None: left_node.parent = node 
        if right_node is not None: right_node.parent = node 
        return node 


    @staticmethod
    def inorder_t(node):
        if node is None:
            return []
        return BSTNode.inorder_t(node.left) + [node, ] + BSTNode.inorder_t(node.right)
        
        


class BST:
    def __init__(self, root=None):
        self.root = root 

    @classmethod
    def _from_arr(cls, arr):
        return cls(BSTNode._from_arr(arr))

    def find_first(self, ):
        if self.root is None: return
        return self.root._left_most_child()

    def _show(self, ):
        nodes = BSTNode.inorder_t(self.root)
        fn = lambda x: (x.item if x is not None else " ")
        print("="*60)
        for i, node in enumerate(nodes):
            print(
                f"{i}: {node.item}, "
                f"parent: {fn(node.parent)}, height: {node.height}, skew: {node.skew}"
            )

    
        








def test():
    try:
        import random 
        # array = [random.randint(0, 10) for _ in range(10)]
        array = [2, 1, 3, 4, 5, 9, 8, 10, 4, 7]
        print(array)
        array = sorted(array)
        bst = BST._from_arr(array)

        print('In order traversal')
        bst._show()
        # this checks for build, height, skew, find next and prev and other functions 

        # next let's check for insert and delete 

        # new_node = BSTNode(9)
        # bst.root.insert_node(new_node)
        # print('node-addes', new_node.item, "parent:", new_node.parent.item) # node-addes 9 parent: 8

        # new_node = BSTNode(6)
        # bst.root.insert_node(new_node)
        # print('node-addes', new_node.item, "parent:", new_node.parent.item) # node-addes 6 parent: 7
        # bst._show()

        # insert prev/next 
        nodes = {i: node for i, node in enumerate(BSTNode.inorder_t(bst.root))}
        # # inserting 9 prev to 9
        # new_node = BSTNode(8.9)
        # nodes[8].insert_prev(new_node)
        # print('node-addes', new_node.item, "parent:", new_node.parent.item)

        # # inserting 6 next to 5
        # new_node = BSTNode(6)
        # nodes[5].insert_next(new_node)
        # print('node-addes', new_node.item, "parent:", new_node.parent.item)

        # # inserting 12 next to 10
        # new_node = BSTNode(12)
        # nodes[9].insert_next(new_node)
        # print('node-addes', new_node.item, "parent:", new_node.parent.item)

        # # inserting 3 prev to 4
        # new_node = BSTNode(3.6)
        # nodes[3].insert_next(new_node)
        # print('node-addes', new_node.item, "parent:", new_node.parent.item, "parent to parent:", new_node.parent.parent.item)

        # new_node = BSTNode(3.5)
        # nodes[4].insert_next(new_node)
        # print('node-addes', new_node.item, "parent:", new_node.parent.item, "parent to parent:", new_node.parent.parent.item)

        # delete 
        # remove 9 and check right of 5 and it's children 
        # nodes[8].remove_node() 
        # print('new right to 5:', nodes[5].right.item)
        # print('new next of 8:', nodes[7].find_next().item)
        # bst._show()

        bst.root.remove_node()
        bst._show()
        



    except:
        import pdb, traceback
        print(traceback.print_exc())
        pdb.set_trace()
test() 