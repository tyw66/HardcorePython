def make_round_pairs(sequece):
    '''
    生成循环配对列表
    '''
    length = len(sequece)
    return [
        (sequece[i], sequece[(i + 1) % length]) 
        for i in range(length)
    ]