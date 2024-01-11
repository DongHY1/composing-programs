def pressure(v,t,n):
    """
    压力计算公式
    """
    k = 1.38e-23  # 玻尔兹曼常数
    return n * k * t / v

help(pressure)