import unittest
from eqs.matrix import Matrix


class MatrixTest(unittest.TestCase):
    def test_is_square(self):
        self.assertTrue(Matrix(3, 3).is_square)

    def test_is_not_square(self):
        self.assertFalse(Matrix(3, 4).is_square)

    def test_init(self):
        m = Matrix(2, 3)
        self.assertEqual(m.row_count, 2)
        self.assertEqual(m.col_count, 3)
        self.assertFalse(m.is_square)

    def test_init_square(self):
        m = Matrix(4, 4)
        self.assertEqual(m.row_count, 4)
        self.assertEqual(m.col_count, 4)
        self.assertTrue(m.is_square)

    def test_row_count_property(self):
        m = Matrix(5, 3)
        self.assertEqual(m.row_count, 5)

    def test_col_count_property(self):
        m = Matrix(3, 5)
        self.assertEqual(m.col_count, 5)

    def test_set_value(self):
        m = Matrix(3, 3)
        m.set_value(2.5, 1, 2)
        self.assertEqual(m._Matrix__data[1][2], 2.5)

    def test_set_value_chained(self):
        m = Matrix(2, 2)
        result = m.set_value(1.0, 0, 0).set_value(2.0, 0, 1).set_value(3.0, 1, 0).set_value(4.0, 1, 1)
        self.assertIs(result, m)
        self.assertEqual(m._Matrix__data, [[1.0, 2.0], [3.0, 4.0]])

    def test_add_value(self):
        m = Matrix(3, 3)
        m.set_value(1.0, 0, 0)
        m.add_value(2.5, 0, 0)
        self.assertEqual(m._Matrix__data[0][0], 3.5)

    def test_add_value_chained(self):
        m = Matrix(2, 2)
        result = m.add_value(1.0, 0, 0).add_value(2.0, 0, 1)
        self.assertIs(result, m)
        self.assertEqual(m._Matrix__data, [[1.0, 2.0], [0.0, 0.0]])

    def test_set_data(self):
        m = Matrix(2, 3)
        m.set_data([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        self.assertEqual(m._Matrix__data, [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

    def test_set_data_chained(self):
        m = Matrix(2, 2)
        result = m.set_data([1.0, 2.0, 3.0, 4.0])
        self.assertIs(result, m)

    def test_set_data_size_mismatch(self):
        m = Matrix(2, 2)
        with self.assertRaises(ValueError):
            m.set_data([1.0, 2.0, 3.0])

    def test_set_data_preserves_independence(self):
        m = Matrix(2, 2)
        external_data = [1.0, 2.0, 3.0, 4.0]
        m.set_data(external_data)
        external_data[0] = 999.0
        self.assertEqual(m._Matrix__data, [[1.0, 2.0], [3.0, 4.0]])

    def test_set_identity_row(self):
        m = Matrix(3, 3)
        m.set_identity_row(1)
        self.assertEqual(m._Matrix__data[1], [0.0, 1.0, 0.0])

    def test_set_identity_col(self):
        m = Matrix(3, 3)
        m.set_identity_col(1)
        self.assertEqual(m._Matrix__data[0][1], 0.0)
        self.assertEqual(m._Matrix__data[1][1], 1.0)
        self.assertEqual(m._Matrix__data[2][1], 0.0)

    def test_value_at(self):
        m = Matrix(2, 3)
        m.set_data([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        self.assertEqual(m.value_at(0, 0), 1.0)
        self.assertEqual(m.value_at(0, 2), 3.0)
        self.assertEqual(m.value_at(1, 1), 5.0)

    def test_value_transposed_at(self):
        m = Matrix(2, 3)
        m.set_data([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        self.assertEqual(m.value_transposed_at(0, 1), 4.0)
        self.assertEqual(m.value_transposed_at(1, 0), 2.0)

    def test_scale(self):
        m = Matrix(2, 2)
        m.set_data([1.0, 2.0, 3.0, 4.0])
        m.scale(2.0)
        self.assertEqual(m._Matrix__data, [[2.0, 4.0], [6.0, 8.0]])

    def test_scale_chained(self):
        m = Matrix(2, 2)
        m.set_data([1.0, 2.0, 3.0, 4.0])
        result = m.scale(2.0)
        self.assertIs(result, m)

    def test_eq_same_object(self):
        m = Matrix(3, 3)
        self.assertEqual(m, m)

    def test_eq_equal_matrices(self):
        m1 = Matrix(2, 3)
        m1.set_data([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        m2 = Matrix(2, 3)
        m2.set_data([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        self.assertEqual(m1, m2)

    def test_eq_different_dimensions(self):
        m1 = Matrix(2, 3)
        m2 = Matrix(3, 2)
        self.assertNotEqual(m1, m2)

    def test_eq_different_values(self):
        m1 = Matrix(2, 2)
        m1.set_data([1.0, 2.0, 3.0, 4.0])
        m2 = Matrix(2, 2)
        m2.set_data([1.0, 2.0, 3.0, 5.0])
        self.assertNotEqual(m1, m2)

    def test_eq_not_matrix(self):
        m = Matrix(2, 2)
        self.assertNotEqual(m, [[0.0, 0.0], [0.0, 0.0]])
        self.assertNotEqual(m, dict())

    def test_initial_all_zeros(self):
        m = Matrix(2, 3)
        for row in range(m.row_count):
            for col in range(m.col_count):
                self.assertEqual(m.value_at(row, col), 0.0)

    def test_scale_zero_factor(self):
        m = Matrix(2, 2)
        m.set_data([1.0, 2.0, 3.0, 4.0])
        m.scale(0.0)
        for row in range(m.row_count):
            for col in range(m.col_count):
                self.assertEqual(m.value_at(row, col), 0.0)

    def test_scale_negative_factor(self):
        m = Matrix(2, 2)
        m.set_data([1.0, 2.0, 3.0, 4.0])
        m.scale(-1.0)
        self.assertEqual(m._Matrix__data, [[-1.0, -2.0], [-3.0, -4.0]])

    def test_add_value_negative_amount(self):
        m = Matrix(3, 3)
        m.set_value(5.0, 0, 0)
        m.add_value(-2.5, 0, 0)
        self.assertEqual(m._Matrix__data[0][0], 2.5)

    def test_set_identity_row_chained(self):
        m = Matrix(3, 3)
        result = m.set_identity_row(0)
        self.assertIs(result, m)

    def test_set_identity_col_chained(self):
        m = Matrix(3, 3)
        result = m.set_identity_col(0)
        self.assertIs(result, m)

