def add(a, b):
    """加法函数"""
    return a + b

def divide(a, b):
    """除法函数"""
    if b == 0:
        raise ValueError("不能除以零！")
    return a / b