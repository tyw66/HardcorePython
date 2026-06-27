from geom2d.nums import are_close_enough
from utils.lists import list_of_list_of_zeros

class Matrix:
    def __init__(self, rows: int, cols: int):
        self.__rows_count = rows
        self.__cols_count = cols
        self.__is_square = rows == cols
        self.__data = list_of_list_of_zeros(rows, cols)

    @property
    def row_count(self) -> int:
        return self.__rows_count

    @property
    def col_count(self) -> int:
        return self.__cols_count

    @property
    def is_square(self) -> bool:
        return self.__is_square
        
    def set_value(self, value: float, row: int, col: int) -> None:
        self.__data[row][col] = value
        return self

    def add_value(self, amount: float, row: int, col: int) -> None:
        self.__data[row][col] += amount
        return self

    def set_data(self, data:[float]):
        if(len(data) != self.__rows_count * self.__cols_count):
            raise ValueError("Cannot set data : size mismatch")
        for row in range(self.__rows_count):
            offset = row * self.__cols_count
            for col in range(self.__cols_count):
                self.__data[row][col] = data[offset + col]
        return self

    def set_identity_row(self, row: int):
        '''
        设置第row行为为单位矩阵的第row行
        '''
        for col in range(self.__cols_count):
            self.__data[row][col] = 1 if col == row else 0
        return self

    def set_identity_col(self, col: int):
        '''
        设置第col列行为为单位矩阵的第col列
        '''
        for row in range(self.__rows_count):
            self.__data[row][col] = 1 if row == col else 0
        return self

    def value_at(self, row:int, col:int):
        return self.__data[row][col]

    def value_transposed_at(self, row:int, col:int):
        return self.__data[col][row]

    def scale(self, factor: float):
        for row in range(self.__rows_count):
            for col in range(self.__cols_count):
                self.__data[row][col] *= factor
        return self

    def __eq__(self, other: 'Matrix') -> bool:
        if self is other:
            return True
        if not isinstance(other, Matrix):
            return False
        if(self.__rows_count != other.__rows_count or self.__cols_count != other.__cols_count):
            return False
        for row in range(self.__rows_count):
            for col in range(self.__cols_count):
                if not are_close_enough(self.__data[row][col], other.__data[row][col]):
                    return False
        return True