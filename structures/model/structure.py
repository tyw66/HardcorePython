from functools import reduce

from .node import StrNode
from .bar import StrBar

class Structure:
    '''结构类'''
    def __init__(self, nodes:list[StrNode], bars:list[StrBar]):
        self.bars = bars
        self.nodes = nodes

    @property
    def node_count(self):
        '''节点数量'''
        return len(self.nodes)

    @property
    def bar_count(self):
        '''梁数量'''
        return len(self.bars)

    @property
    def loads_count(self):
        '''载荷数量'''
        return sum(node.loads_count for node in self.nodes)