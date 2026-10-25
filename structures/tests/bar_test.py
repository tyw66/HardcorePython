import unittest
from math import sqrt

from eqs import Matrix
from geom2d import Point
from structures import StrNode
from structures import StrBar  

class BarTest(unittest.TestCase):
    section = sqrt(5)
    young_mod = 5
    node_a = StrNode(1, Point(0, 0))
    node_b = StrNode(2, Point(2, 1))
    bar = StrBar(1, node_a, node_b, section, young_mod)

    def test_global_stiffness_matrix(self):
        '''测试全局刚度矩阵'''
        expected =  Matrix(4, 4).set_data([
            4,2,-4,-2,
            2,1,-2,-1,
            -4,-2,4,2,
            -2,-1,2,1
        ])
        actual = self.bar.global_stiffness_matrix()
        self.assertEqual(actual, expected)
