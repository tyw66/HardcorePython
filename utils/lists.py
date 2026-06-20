def list_of_zeros(length: int) -> list:
    return [0] * length

def list_of_list_of_zeros(rows:int, col:int) -> list:
    return [list_of_zeros(col) for _ in range(rows)]
