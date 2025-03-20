from collections import deque
from typing import Deque, Optional
import graphviz as gv
from .node import Node, NodeColor, node_color, parent
from .tree import Tree

class TreeGraph:
    def __init__(self, tree: Tree):
        self._tree: Tree = tree
        self._graph: gv.Digraph = gv.Digraph('Red Black Tree')
        self._graph.attr(rankdir='TB')
        self._nil_count: int = 0
    
    def build(self) -> None:
        """"""
        if not self._tree.root:
            raise ValueError('Cannot build graph for an empty Red Black Tree')
        
        self._graph.clear()
        self._nil_count = 0
        node_q: Deque[Optional[Node]] = deque()
        node_q.append(self._tree.root)
        
        while node_q:
            n: Optional[Node] = node_q.popleft()
            p: Optional[Node] = parent(n)
            self._add_node(n, p)
            if n:
                node_q.append(n.left_child)
                node_q.append(n.right_child)
    
    def view(self) -> None:
        self._graph.view()
    
    def _add_node(self, node: Optional[Node], parent: Optional[Node]) -> Node:
        """"""
        if not node:
            if not parent:
                return

            parent_id: str = str(parent.key)
            leaf_id: str = f'NIL{self._nil_count}'
            self._nil_count += 1
            self._graph.node(leaf_id, style='filled', fillcolor='black', fontcolor='white')
            self._graph.edge(parent_id, leaf_id)
            return
        
        node_id: str = str(node.key)
        color: str = str(node.color).lower().split('.')[1]
        self._graph.node(node_id, style='filled', fillcolor=color, fontcolor='white')
        
        if parent:
            parent_id: str = str(parent.key)
            self._graph.edge(parent_id, node_id)
