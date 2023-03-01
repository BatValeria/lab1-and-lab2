"""
My little Queue
"""
from typing import Any


class Queue:  # O(1)
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self.list_ = [5, 3, 7]  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:  # O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        return self.list_.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:  # O(1)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста
        :return: Извлеченный с начала очереди элемент.
        """
        if not self.list_:  # TODO реализовать метод dequeue
            raise IndexError  # O(1)

        return self.list_.pop(0)

    def peek(self, ind: int = 0) -> Any:  # O(n)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):  # TODO реализовать метод peek
            raise TypeError

        if len(self.list_) - 1 < ind < 0:
            raise IndexError

        return self.list_[ind]

    def clear(self) -> None:  # O(1)
        """ Очистка очереди. """
        return self.list_.clear()  # TODO реализовать метод clear

    def __len__(self):  # O(1)
        """ Количество элементов в очереди. """
        return self.list_.__len__()  # TODO реализовать метод __len__
