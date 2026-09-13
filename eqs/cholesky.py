import math
from eqs.matrix import Matrix
from eqs.vector import Vector

def cholesky_solve(sys_mat:Matrix, sys_vec : Vector):
    '''执行Cholesky分解法求解线性方程组 Ax = b，其中A为对称正定矩阵，b为向量'''
    validate_system(sys_mat, sys_vec)
    low_matrix = lower_matrix_decomposition(sys_mat)
    low_solution = solve_lower_sys(low_matrix, sys_vec)
    return solve_upper_sys(low_matrix, low_solution)


def validate_system(sys_matrix:Matrix, sys_vec : Vector):
    '''验证线性方程组的有效性，确保矩阵和向量的维度匹配，并且矩阵是方阵'''
    if sys_matrix.col_count != sys_vec.length:
        raise ValueError("Size mismatch between matrix and vector")
    
    if not sys_matrix.is_square:
        raise ValueError("System matrix is not square")

def lower_matrix_decomposition(sys_matrix:Matrix):
    '''对称正定矩阵的Cholesky分解，返回下三角矩阵L，使得A = L * L^T'''
    n = sys_matrix.row_count
    low_matrix = Matrix(n, n)
    for i in range(n):
        sq_num = 0
        for j in range(i + 1):
            m_ij = sys_matrix.value_at(i, j)

            if i==j:
                diag_val = math.sqrt(m_ij - sq_num)
                low_matrix.set_value(diag_val, i, j)

            else:
                non_diag_sum = 0
                for k in range(j):
                    l_ik = low_matrix.value_at(i, k)
                    l_jk = low_matrix.value_at(j, k)
                    non_diag_sum += l_ik * l_jk
                l_jj = low_matrix.value_at(j, j)
                non_diag_val = (m_ij - non_diag_sum) / l_jj
                low_matrix.set_value(non_diag_val, i, j)
                
                sq_num += non_diag_val ** 2
                
    return low_matrix


def solve_lower_sys(low_matrix:Matrix, sys_vec : Vector):
    '''求解下三角矩阵L * x = b，返回向量solution'''
    size = sys_vec.length
    solution = Vector(size)

    for i in range(size):
        acc = sys_vec.value_at(i)
        for j in range(i):
            acc -= low_matrix.value_at(i, j) * solution.value_at(j)
        solution.set_value(acc / low_matrix.value_at(i, i), i)
    return solution


def solve_upper_sys(low_matrix:Matrix, sys_vec : Vector):
    '''求解上三角矩阵L^T * x = b，返回向量solution'''
    size = sys_vec.length
    solution = Vector(size)
    for i in range(size - 1, -1, -1):
        acc = sys_vec.value_at(i)
        for j in range(i + 1, size):
            acc -= low_matrix.value_transposed_at(i, j) * solution.value_at(j)
        solution.set_value(acc / low_matrix.value_transposed_at(i, i), i)
    return solution