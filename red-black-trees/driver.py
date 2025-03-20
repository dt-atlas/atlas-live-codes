#!/usr/bin/env python3

from typing import Tuple
import redblacklib
from redblacklib.node import Node, NodeColor, aunt, grandparent, node_color, parent
from redblacklib.graph import TreeGraph

if __name__ == '__main__':
    keys: Tuple[int] = 98, 402, 512, 12, 46, 128, 256, 1, 624, 780
    tree: redblacklib.Tree = redblacklib.Tree()
    # for k in keys:
    #     node = tree.insert(k)
    #     print(node)
    
    # Level 1
    tree.root = Node(98, NodeColor.BLACK)
    p: Node = tree.root
    
    # Level 2
    tmp: Node = Node(12, NodeColor.RED, p)
    p.left_child = tmp
    tmp = Node(402, NodeColor.RED, p)
    p.right_child = tmp
    
    # Level 3A
    p = p.left_child
    tmp = Node(6, NodeColor.BLACK, p)
    p.left_child = tmp
    tmp = Node(16, NodeColor.BLACK, p)
    p.right_child = tmp
    
    # Level 3B
    p = p.parent.right_child
    tmp = Node(256, NodeColor.BLACK, p)
    p.left_child = tmp
    tmp = Node(512, NodeColor.BLACK, p)
    p.right_child = tmp
    
    graph = TreeGraph(tree)
    graph.build()
    graph.view()
