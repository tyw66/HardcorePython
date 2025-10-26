def make_round_pairs(sequece):
    '''
    生成循环配对列表
    eg. sequece = [A,B,C,D]  return [(A,B),(B,C),(C,D),(D,A)]
    '''
    length = len(sequece)
    return [
        (sequece[i], sequece[(i + 1) % length]) 
        for i in range(length)
    ]