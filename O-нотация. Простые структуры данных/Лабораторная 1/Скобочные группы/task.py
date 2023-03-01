def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, Fals e в противном случае
    """

    box = 0

    for bracket in brackets_row:
        if bracket == "(":
            box += 1
        else:
            box -= 1
            if box < 0:
                return False

    if box == 0:
        return True


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
