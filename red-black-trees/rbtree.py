#!/usr/bin/env python3

from dataclasses import dataclass
from enum import IntEnum
from typing import Optional, Tuple
import graphviz as gv

class NodeColor(IntEnum):
    """Enumeration of node colors in a red-black tree"""
    BLACK = 0
    RED = 1

@dataclass
class RBTreeNode:
    """"""
    key: int
    color: NodeColor = NodeColor.RED
    parent: Optional['RBTreeNode'] = None
    left_child: Optional['RBTreeNode'] = None
    right_child: Optional['RBTreeNode'] = None
    
    def __str__(self) -> str:
        return f'RBTreeNode: Key={self.key} Color={str(self.color)}'
    
    @property
    def height(self) -> int:
        """Height of the subtree"""
        pass
    
    def insert(self, key: int) -> Tuple[bool, 'RBTreeNode']:
        """Insert key into the node's subtree"""
        leader, follower = self, None
        while leader:
            if key == leader.key:  # Key already in tree
                return False, leader
            follower = leader
            leader = leader.left_child if key < leader.key else leader.right_child
        
        # follower is now parent of the new node
        new_node = RBTreeNode(key, color=NodeColor.RED, parent=follower)
        if key < follower.key:
            follower.left_child = new_node
        else:
            follower.right_child = new_node
        
        return True, new_node

    def rotate_left(self) -> 'RBTreeNode':
        """"""
        # Establish right_child as new root of subtree
        new_root = self.right_child
        self.right = new_root.left_child
        # Relink children and parents
        if new_root.left_child:
            new_root.left_child.parent = self
        new_root.parent = self.parent
        if self.is_left_child:
            self.parent.left_child = new_root
        else:
            self.parent.right_child = new_root
        new_root.left_child = self
        self.parent = new_root
        return new_root
    
    def rotate_right(self) -> 'RBTreeNode':
        """"""
        # Establish left_child as new root of subtree
        new_root = self.left_child
        self.left = new_root.right_child
        # Relink children and parents
        if new_root.right_child:
            new_root.right_child.parent = self
        new_root.parent = self.parent
        if self.is_right_child:
            self.parent.right_child = new_root
        else:
            self.parent.left_child = new_root
        new_root.right_child = self
        self.parent = new_root
        return new_root
    
    @property
    def is_left_child(self):
        if not self.parent:
            return False
        return id(self) == id(self.parent.left_child)
    
    @property
    def is_right_child(self):
        if not self.parent:
            return False
        return id(self) == id(self.parent.right_child)


class RedBlackTree:
    """"""
    def __init__(self):
        self.root: Optional['RBTreeNode'] = None

    def insert(self, key: int) -> RBTreeNode:
        """Inserts a key into the tree"""
        if not self.root:
            self.root = RBTreeNode(key, color=NodeColor.BLACK)
            return self.root
        
        key_added, new_node = self.root.insert(key)
        
        if key_added:
            self._insert_fixup(new_node)
        
        return new_node

    def delete(self, key: int) -> RBTreeNode:
        """"""
        pass
    
    def render_diagram(self) -> None:
        """"""
        def node_graph_id(node: Optional[RBTreeNode]) -> Optional[str]:
            if not node:
                return None
            return f'{str(node.color)[0]}({node.key})'
        
        def traverse_edges(node: Optional[RBTreeNode]) -> None:
            """"""
            if not node:
                return

            # node_color = str(node.color).lower()
            node_id = node_graph_id(node)
            left_id = node_graph_id(node.left_child)
            right_id = node_graph_id(node.right_child)
            print(f'{node_id} left={left_id} right={right_id}')
            
            # graph.node_attr.update(style='fill', color=node_color)
            
            if left_id:
                graph.edge(node_id, left_id)
            if right_id:
                graph.edge(node_id, right_id)
            
            traverse_edges(node.left_child)
            traverse_edges(node.right_child)
            
        graph = gv.Digraph('red_black_tree', filename='rbtree.gv')
        graph.attr('node', shape='circle')
        traverse_edges(self.root)
        graph.view()
    
    def _insert_fixup(self, node: RBTreeNode) -> None:
        """Restores RB property from new node back up to the root"""
        aunt: Optional[RBTreeNode] = None
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
                node = node.rotate_right()
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
                node = node.rotate_left()
        
        self.root.color = NodeColor.BLACK

    def _delete_fixup(self, x: RBTreeNode) -> None:
        """Restores RB property from root downward"""
        pass


def node_color(node_ptr: Optional[RBTreeNode]) -> NodeColor:
    """Tiny abstraction to support nodes and black leaves"""
    return node_ptr.color if node_ptr else NodeColor.BLACK


def parent(node_ptr: Optional[RBTreeNode]) -> NodeColor:
    """Tiny abstraction to simplify parent fetching"""
    return node_ptr.parent if node_ptr else None


def grandparent(node_ptr: Optional[RBTreeNode]) -> Optional[RBTreeNode]:
    """Tiny abstraction to simplify grandparent fetching"""
    p = parent(node_ptr)
    return parent(p)


def aunt(node_ptr: Optional[RBTreeNode]) -> Optional[RBTreeNode]:
    """Tiny abstraction to simplify uncle fetching"""
    p = parent(node_ptr)
    gp = parent(p)
    return gp.left_child if p.is_right_child else gp.right_child
    

if __name__ == '__main__':
    keys: Tuple[int] = 98, 402, 512, 12, 46, 128, 256, 1, 624, 780
    tree: RedBlackTree = RedBlackTree()
    new_node: Optional[RBTreeNode] = None
    # for i, k in enumerate(keys):
    #     print(f'\nInserting key no. {i + 1}: {k}')
    #     new_node = tree.insert(k)
    #     print(f'new_node: {new_node}')
    #     print(f'new_node.parent: {new_node.parent}')
    for k in keys:
        new_node = tree.insert(k)
    
    tree.render_diagram()
    
        

# Inserting key no. 1: 98
# new_node: RBTreeNode: Key=98 Color=NodeColor.BLACK
# new_node.parent: None

# Inserting key no. 2: 402
# new_node: RBTreeNode: Key=402 Color=NodeColor.RED
# new_node.parent: RBTreeNode: Key=98 Color=NodeColor.BLACK

# Inserting key no. 3: 512
# new_node: RBTreeNode: Key=512 Color=NodeColor.RED
# new_node.parent: RBTreeNode: Key=98 Color=NodeColor.BLACK

# Inserting key no. 4: 12
# new_node: RBTreeNode: Key=12 Color=NodeColor.RED
# new_node.parent: RBTreeNode: Key=98 Color=NodeColor.BLACK

# Inserting key no. 5: 46
# new_node: RBTreeNode: Key=46 Color=NodeColor.RED
# new_node.parent: RBTreeNode: Key=98 Color=NodeColor.BLACK

# Inserting key no. 6: 128
# new_node: RBTreeNode: Key=128 Color=NodeColor.RED
# new_node.parent: RBTreeNode: Key=98 Color=NodeColor.BLACK

# Inserting key no. 7: 256
# new_node: RBTreeNode: Key=256 Color=NodeColor.RED
# new_node.parent: RBTreeNode: Key=98 Color=NodeColor.BLACK

# Inserting key no. 8: 1
# new_node: RBTreeNode: Key=1 Color=NodeColor.RED
# new_node.parent: RBTreeNode: Key=98 Color=NodeColor.BLACK

# Inserting key no. 9: 624
# new_node: RBTreeNode: Key=624 Color=NodeColor.RED
# new_node.parent: RBTreeNode: Key=98 Color=NodeColor.BLACK

# Inserting key no. 10: 780
# new_node: RBTreeNode: Key=780 Color=NodeColor.RED
# new_node.parent: RBTreeNode: Key=98 Color=NodeColor.BLACK
