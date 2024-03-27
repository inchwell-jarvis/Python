# 接收传入参数。将参数翻转后返回

def reverse_string(input_str):
    """
    将输入字符串翻转并返回。

    参数：
    input_str (str): 要翻转的字符串。

    返回：
    str: 翻转后的字符串。
    """
    return input_str[::-1]


def substr(s, x, y):
    """
    :param s: 字符串

    :param x: 切片开始下标

    :param y: 切片结束下标

    :return: 返回值
    """
    return s[x, y]
