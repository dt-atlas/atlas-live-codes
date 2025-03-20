from dataclasses import dataclass
from enum import IntEnum
from typing import Optional, Tuple
import graphviz as gv


class NodeColor(IntEnum):
    """Enumeration of node colors in a red-black tree"""
    BLACK = 0
    RED = 1


@dataclass
class Node:
    """"""
    key: int
    color: NodeColor = NodeColor.RED
    parent: Optional['Node'] = None
    left_child: Optional['Node'] = None
    right_child: Optional['Node'] = None
    
    def __str__(self) -> str:
        """String representation of the node"""
        return f'RBTreeNode: Key={self.key} Color={str(self.color)}'
    
    @property
    def height(self) -> int:
        """Height of the subtree"""
        pass
    
    def insert(self, key: int) -> Tuple[bool, 'Node']:
        """Insert key into the node's subtree"""
        leader, follower = self, None
        while leader:
            if key == leader.key:  # Key already in tree
                return False, leader
            follower = leader
            leader = leader.left_child if key < leader.key else leader.right_child
        
        # follower is now parent of the new node
        new_node = Node(key, color=NodeColor.RED, parent=follower)
        if key < follower.key:
            follower.left_child = new_node
        else:
            follower.right_child = new_node
        
        return True, new_node

    def rotate_left(self) -> 'Node':
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
    
    def rotate_right(self) -> 'Node':
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


# Helper functions


def node_color(node_ptr: Optional[Node]) -> Optional[Node]:
    """Tiny abstraction to support nodes and black leaves"""
    return node_ptr.color if node_ptr else NodeColor.BLACK


def parent(node_ptr: Optional[Node]) -> Optional[Node]:
    """Tiny abstraction to simplify parent fetching"""
    return node_ptr.parent if node_ptr else None


def grandparent(node_ptr: Optional[Node]) -> Optional[Node]:
    """Tiny abstraction to simplify grandparent fetching"""
    p = parent(node_ptr)
    return parent(p)


def aunt(node_ptr: Optional[Node]) -> Optional[Node]:
    """Tiny abstraction to simplify uncle fetching"""
    p = parent(node_ptr)
    gp = parent(p)
    return gp.left_child if p.is_right_child else gp.right_child
