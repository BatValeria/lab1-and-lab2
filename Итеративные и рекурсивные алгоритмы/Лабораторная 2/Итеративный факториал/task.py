def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    final = 1
    if n == 1:
        return final

    if n < 0:
        raise ValueError

    for next_param in range(1, n + 1):
        final *= next_param
    return final
