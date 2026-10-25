import operator
from functools import reduce    

from geom2d import Point,Vector

class StrNode:
    '''结构节点类'''
    def __init__(self, _id:int, position:Point, loads=None, dx_constraint=False, dy_constraint=False):
        self._id = _id
        self.position = position
        self.loads = loads or []
        self.dx_constraint = dx_constraint
        self.dy_constraint = dy_constraint

    @property
    def loads_count(self):
        '''节点上的载荷数量'''
        return len(self.loads)

    @property
    def net_load(self):
        '''计算节点上的载荷总和'''
        return reduce(
            operator.add,
            self.loads,
            Vector(0, 0)
        )

    def add_load(self, load:Vector):
        '''添加载荷'''
        self.loads.append(load)

    def __eq__(self, other):
        '''节点相等'''
        if self is other:
            return True
        if not isinstance(other, StrNode):
            return False
        return self.position == other.position


   