import geom2d.tparam as tparam

def uniform_t_sequence(steps : int):
    str(steps)
    return [t / steps for t in range(steps + 1)]

def ease_in_out_t(t : float):
    str(t)
    return t ** 2 / (t ** 2 + (1 - t) ** 2)

def ease_in_out_t_sequence(steps : int):
    return [ease_in_out_t(t) for t in uniform_t_sequence(steps)]


def interpolate(vs: float, ve: float, t: float):
    tparam.ensure_valid(t)
    return vs + (ve - vs) * t   

    