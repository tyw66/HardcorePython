MIN = 0.0
MIDDLE = 0.5
MAX = 1.0

def make(value: float) -> float:
    '''创建参数值，确保其在 [0, 1] 范围内'''
    if value < MIN :
        return MIN
    if value > MAX:
        return MAX
    return value

def is_valid(t) -> bool:
    return False if t< MIN or t> MAX else True

def ensure_valid(t):
    if not is_valid(t):
        raise TParamError(t)
    

class TParamError(Exception):
    def __init__(self, t):
        self.t =t
        
    def __str__(self) -> str:
        return f'TParamError: t value {self.t} is out of range [0.0, 1.0]'