class Node:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return f'key:{self.key}, data:{self.data}, l:{self.left}, r:{self.right}'

class BST:

    def __init__(self):
        self.root = None

    def search(self, key) -> Node.data:
        if self.root is None:
            return None
        node = self.root
        node = self.__search(key, node)
        if node is None:
            return node
        return node.data

    def __search(self, key, node) -> Node:
        if node is None:
            return node
        if node.key < key:
            return self.__search(key, node.right)
        elif node.key > key:
            return self.__search(key, node.left)
        else:
            return node

    
    def insert(self, key, data) -> None:
        if self.root is None:
            self.root = Node(key, data)
        else:
            node = self.root
            self.__insert(key, data,node)

    def __insert(self, key, data, node) -> Node:
        if node is None:
            return Node(key, data)
        if node.key == key:
            node.data = data
            return node
        elif node.key > key:
            node.left = self.__insert(key, data, node.left)
            return node
        elif node.key < key:
            node.right = self.__insert(key, data, node.right)
            return node


    def delete(self, key) -> str:
        node = self.root
        if node is None:
            return 'Element with that key not found'
        return self.__delete(node, key)

    def __delete(self, node, key) -> Node:
        if node.key > key:
            node.left = self.__delete(node.left, key)
        elif node.key < key:
            node.right = self.__delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                return temp 
            elif node.right is None:
                temp = node.left
                return temp  

            temp = node.right
            while temp.left is not None:
                temp = temp.left

            node.key = temp.key
            node.data = temp.data
            node.right = self.__delete(node.right, temp.key)

        return node

    def print(self) -> str:
        return self.__print(self.root)
    
    def __print(self, node):
        if node.left:
            self.__print(node.left)
        print(f"{node.key} : {node.data}", end=', ')
        if node.right:
            self.__print(node.right)


    def height(self, start_key=None) -> int:
        if start_key is None:
            start_key = self.root.key
        node = self.root
        if node.key != start_key:
            return self.__height(self.__go_to_node(start_key, node))
        return self.__height(node)

    def __height(self, node) -> int:
        if node is None:
            return -1
        else:
            left_height = self.__height(node.left)
            right_height = self.__height(node.right)
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
            
    def __go_to_node(self, start_key, node) -> Node:
        if node.key == start_key:
            return node
        if start_key < node.key:
            return self.__go_to_node(start_key, node.left)
        if start_key > node.key:
            return self.__go_to_node(start_key, node.right)
    
    def print_tree(self) -> str:
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl) -> str:
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left, lvl+5)

tree = BST()
el = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
for i in el.keys():

    tree.insert(i, el[i])

tree.print_tree()
tree.print()
print(tree.search(24))
tree.insert(20, 'AA')
tree.insert(6, 'M')
tree.delete(62)
tree.insert(59, 'N')
tree.insert(100, 'P')
tree.delete(8)
tree.delete(15)
tree.insert(55, 'R')
tree.delete(50)
tree.delete(5)
tree.delete(24)
print(tree.height())
tree.print()
tree.print_tree()