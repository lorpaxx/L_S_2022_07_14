# 2. На языках Python(2.7) и/или С++,
# написать минимум по 2 класса реализовывающих циклический буфер.
# Объяснить плюсы и минусы каждой реализации.

# Циклитческий буфер, реализованный на массиве фиксированной длины
# +
# память тратися только на все элементы массива (если они не None),
# индекс стартовой и индекс конечной позиции
# -
# для добавления/удаления элемента буфера нужно больше действий
# по сравнению с CycleBuferLinkedList, хотя они и не более затратны по времени
class CycleBufer:
    '''
    Класс CycleBufer.
    '''
    def __init__(self, size=7) -> None:
        '''
        Создаём буфер.
        size - размер буфера
        '''
        if isinstance(size, int) and size > 0:
            self.size = size
            self.array = [None] * self.size
            self.begin = None
            self.end = None
            self.lenght = 0
        else:
            raise ValueError('size must be >= 0!!!')

    def __add_first(self, value):
        '''
        Добавляем первый элемент в буфер.
        '''
        self.begin = 0
        self.end = 0
        self.array[self.begin] = value
        self.lenght = 1

    def __add_last(self, value):
        '''
        Добавление элемента в буфер при условии, что буфер полон.
        '''
        self.begin = (self.begin + 1) % self.size
        self.end = (self.end + 1) % self.size
        self.array[self.end] = value

    def add(self, value):
        '''
        Добавить элемент в буфер.
        '''
        if self.lenght == self.size:
            self.__add_last(value)
        elif self.lenght == 0:
            self.__add_first(value)
        else:
            self.end = (self.end + 1) % self.size
            self.array[self.end] = value
            self.lenght += 1

    def __remove_one(self):
        '''
        Удалить единсвенный элемент из буфера.
        '''
        value = self.array[self.begin]
        self.array[self.begin] = None
        self.begin = None
        self.end = None
        self.lenght = 0
        return value

    def remove(self):
        '''
        Удалить элемент из буфера.
        '''
        if self.lenght == 0:
            raise ValueError('Bufer is empty')
        if self.lenght == 1:
            return self.__remove_one()
        value = self.array[self.begin]
        self.array[self.begin] = None
        self.begin = (self.begin + 1) % self.size
        self.lenght -= 1
        return value


# Циклический буфер, реализованный на связанном списке
# +
# для добавления/удаления элемента буфера нужно меньше действий
# по сравнению с CycleBufer.
# -
# Нужно больше памяти для хранения объектов класса Node кроме value в них.
class CycleBuferLinkedList:
    '''
    Класс CycleBuferLinkedList.
    '''
    class Node:
        '''
        Класс Node.
        '''
        def __init__(self, value=None, last=None, post=None) -> None:
            self.value = value
            self.last = last
            self.post = post

        def __repr__(self) -> str:
            return str(self.value)

        def __str__(self) -> str:
            return str(self.value)

    def __init__(self, size=7) -> None:
        '''
        Создаём буфер.
        size - размер буфера, дожен быть больше 0
        '''
        if isinstance(size, int) and size > 0:
            self.lenght = 0
            self.begin = self.Node()
            self.end = self.begin
            self.size = size
            last_node = self.begin
            for _ in range(1, self.size):
                node = self.Node(last=last_node)
                last_node.post = node
                last_node = node
            last_node.post = self.begin
            self.begin.last = last_node
        else:
            raise ValueError('size must be >= 0!!!')

    def __add_first(self, value):
        '''
        Добавляем первый элемент в буфер.
        '''
        self.begin.value = value
        self.lenght = 1

    def __add_last(self, value):
        '''
        Перезаписываем самый старый элемент при переполнении.
        '''
        self.begin = self.begin.post
        self.end = self.end.post
        self.end.value = value

    def add(self, value):
        '''
        Добавить элемент в буфер.
        '''
        if self.lenght == 0:
            self.__add_first(value)
        elif self.lenght == self.size:
            self.__add_last(value)
        else:
            self.end = self.end.post
            self.end.value = value
            self.lenght += 1

    def __remove_one(self):
        '''
        Удалить единственный элемент из буфера.
        '''
        value = self.begin.value
        self.begin.value = None
        self.begin = self.begin.post
        self.end = self.begin
        self.lenght = 0
        return value

    def remove(self):
        '''
        Удалить элемент из буфера.
        '''
        if self.lenght == 0:
            raise ValueError('Bufer is empty')
        if self.lenght == 1:
            return self.__remove_one()
        value = self.begin.value
        self.begin.value = None
        self.begin = self.begin.post
        self.lenght -= 1
        return value

    def __str__(self) -> str:
        arr = [''] * self.size
        node = self.begin
        for i in range(self.size):
            arr[i] = str(node.value)
            node = node.post
        return '->'.join(arr)


def test_CycleBufer():
    try:
        bufer = CycleBufer(0)
    except ValueError as e:
        print(e)

    bufer = CycleBufer(5)

    try:
        bufer.remove()
    except ValueError as e:
        print(e)

    bufer.add(3)
    bufer.add(4)
    bufer.add(5)
    bufer.add(1)
    bufer.add(2)
    assert bufer.remove() == 3

    bufer.add(6)
    bufer.add(7)

    # assert bufer.remove() == 4
    assert bufer.remove() == 5
    assert bufer.remove() == 1
    assert bufer.remove() == 2
    assert bufer.remove() == 6
    assert bufer.remove() == 7
    try:
        bufer.remove()
    except ValueError as e:
        print(e)
    bufer.add(3)
    bufer.add(4)
    bufer.add(5)
    assert bufer.remove() == 3
    assert bufer.remove() == 4
    assert bufer.remove() == 5


def test_CycleBuferLinkedList():
    try:
        bufer = CycleBuferLinkedList(0)
    except ValueError as e:
        print(e)
    bufer = CycleBuferLinkedList(5)
    bufer.add(3)
    bufer.add(4)
    bufer.add(5)
    bufer.add(1)
    bufer.add(2)
    assert bufer.remove() == 3
    bufer.add(6)
    bufer.add(7)

    assert bufer.remove() == 5
    assert bufer.remove() == 1
    assert bufer.remove() == 2
    assert bufer.remove() == 6
    assert bufer.remove() == 7
    try:
        bufer.remove()
    except ValueError as e:
        print(e)
    bufer.add(3)
    bufer.add(4)
    bufer.add(5)
    assert bufer.remove() == 3
    assert bufer.remove() == 4
    assert bufer.remove() == 5


def test_time():
    from random import randint
    from time import time
    n = 10 ** 5
    start1 = time()
    bufer1 = CycleBufer(n)
    for _ in range(2 * n):
        bufer1.add(randint(0, n))
    for _ in range(n):
        bufer1.remove()
    stop1 = time()
    del(bufer1)
    start2 = time()
    bufer2 = CycleBuferLinkedList(n)
    for _ in range(2 * n):
        bufer2.add(randint(0, n))
    for _ in range(n):
        bufer2.remove()
    stop2 = time()
    del(bufer2)
    print(
        f'n = {n}, CycleBufer: time - {stop1 - start1} cek')
    print(
        f'n = {n}, CycleBuferLinkedList:'
        f'time - {stop2 - start2} cek')


if __name__ == '__main__':
    test_CycleBufer()
    test_CycleBuferLinkedList()
    test_time()
