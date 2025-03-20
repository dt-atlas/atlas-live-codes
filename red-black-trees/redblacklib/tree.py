import graphviz as gv
from typing import Optional
from .node import Node, NodeColor
from .node import aunt, grandparent, node_color, parent

class Tree:
    """"""
    def __init__(self):
        self.root: Optional['Node'] = None

    def insert(self, key: int) -> Node:
        """Inserts a key into the tree"""
        if not self.root:
            self.root = Node(key, color=NodeColor.BLACK)
            return self.root
        
        key_added, new_node = self.root.insert(key)
        
        if key_added:
            self._insert_fixup(new_node)
        
        return new_node

    def delete(self, key: int) -> Node:
        """"""
        pass
    
    def _insert_fixup(self, node: Node) -> None:
        """Restores RB property from new node back up to the root"""
        aunt: Optional[Node] = None
        while node_color(node.parent) == NodeColor.RED:
            p = node.parent
            gp = grandparent(node)
            if p.is_left_child:
                aunt = gp.right_child
                # Case 1
                if node_color(aunt) == NodeColor.RED:
                    p.color = NodeColor.BLACK
                    aunt.color = NodeColor.BLACK
                    gp.color = NodeColor.RED
                    node = gp
                # Case 2
                elif node.is_right_child:
                    node = node.parent
                    node = node.rotate_left()
                # Case 3 (but shared by all)
                p.color = NodeColor.BLACK
                gp.color = NodeColor.RED
                gp.rotate_right()
            else: # mirror of previous branch
                aunt = gp.left_child
                # Case 1
                if node_color(aunt) == NodeColor.RED:
                    p.color = NodeColor.BLACK
                    aunt.color = NodeColor.BLACK
                    gp.color = NodeColor.RED
                    node = gp
                # Case 2
                elif node.is_left_child:
                    node = node.parent
                    node = node.rotate_right()
                # Case 3 (but shared by all)
                p.color = NodeColor.BLACK
                gp.color = NodeColor.RED
                gp.rotate_left()
        
        self.root.color = NodeColor.BLACK

    def _delete_fixup(self, x: Node) -> None:
        """Restores RB property from root downward"""
        pass
