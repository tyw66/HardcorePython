import unittest

from eqs.cholesky import cholesky_solve, lower_matrix_decomposition, solve_lower_sys, solve_upper_sys, validate_system
from eqs.matrix import Matrix
from eqs.vector import Vector


class CholeskyTest(unittest.TestCase):
    def setUp(self):
        # 对称正定矩阵（A = L * L^T），注意 A[1][3] 与 A[3][1] 均为 -7
        self.sys_matrix = Matrix(4, 4).set_data([
            4, -2, 4, 2,
            -2, 10, -2, -7,
            4, -2, 8, 4,
            2, -7, 4, 7
        ])
        self.sys_vec = Vector(4).set_data([8, 2, 16, 6])
        self.low_matrix = Matrix(4, 4).set_data([
            2, 0, 0, 0,
            -1, 3, 0, 0,
            2, 0, 2, 0,
            1, -2, 1, 1
        ])
        self.low_solution = Vector(4).set_data([4, 2, 4, 2])
        self.solution = Vector(4).set_data([1, 2, 1, 2])

    def test_validate_system_ok(self):
        self.assertIsNone(validate_system(self.sys_matrix, self.sys_vec))

    def test_validate_system_size_mismatch(self):
        bigger_vec = Vector(5)
        with self.assertRaises(ValueError):
            validate_system(self.sys_matrix, bigger_vec)

    def test_validate_system_not_square(self):
        not_square = Matrix(2, 4)
        with self.assertRaises(ValueError):
            validate_system(not_square, Vector(4))

    def test_lower_matrix_decomposition(self):
        actual = lower_matrix_decomposition(self.sys_matrix)
        self.assertEqual(self.low_matrix, actual)

    def test_solve_lower_sys(self):
        actual = solve_lower_sys(self.low_matrix, self.sys_vec)
        self.assertEqual(self.low_solution, actual)

    def test_solve_upper_sys(self):
        actual = solve_upper_sys(self.low_matrix, self.low_solution)
        self.assertEqual(self.solution, actual)

    def test_cholesky_solve(self):
        actual = cholesky_solve(self.sys_matrix, self.sys_vec)
        self.assertEqual(self.solution, actual)


if __name__ == '__main__':
    unittest.main()
