from geom2d.nums import are_close_enough
from utils.lists import list_of_zeros

class Vector:
    def __init__(self, length: int):
        self.__length = length
        self.__data = list_of_zeros(length)
    
    @property
    def length(self) -> int:
        return self.__length

    def set_value(self, value: float, index: int):
        self.__data[index] = value
        return self

    def add_to_value(self, amount:float, index:int):
        self.__data[index] += amount    
        return self

    def set_data(self, data:list[float]):
        if len(data) != self.__length:
            raise ValueError("cannot set data: length mismatch")        
        for i in range(self.__length):
            self.__data[i] = data[i]       
        return self

    def value_at(self, index: int) -> float:
        return self.__data[index]
        
    def __eq__(self, other:'Vector'):
        if self is other:
            return True
        
        if not isinstance(other, Vector):
            return False

        if self.__length != other.__length:
            return False
        for i in range(self.__length):
            if not are_close_enough(self.__data[i], other.__data[i]):
                return False

        return True
