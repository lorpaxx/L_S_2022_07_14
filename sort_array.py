from typing import List

# Алгоритм пирамидальной сортировки
# +
# выполяняется за O(N*log(N)) в любой ситуации, что, мне кажется
# и требуется по условию, вроде быстрее то и не получится на больших массивах
# -
# выполяняется за O(N*log(N)) в любой ситуации (даже отсортированный
# массив обрабатывать будет.
# неустойчив, что в ряде случаев критично


def heapsort(array: List[int]) -> None:
    '''
    Пирамидальная сортировка.
    Принимает на вход List[int] и сортирует его по возрастанию.
    '''
    def parent(i):
        '''Находим индекс родителя.'''
        return (i - 1) // 2

    def left(i):
        '''Находим индекс потомка слева.'''
        return 2 * i + 1

    def right(i):
        '''Находим индекс потомка справа.'''
        return 2 * i + 2

    def build_max_heap(array):
        '''Строим максимальное сортирующее дерево.'''
        length = len(array)
        start = parent(length - 1)
        while start >= 0:
            max_heapify(array, index=start, size=length)
            start = start - 1

    def max_heapify(array, index, size):
        '''Перестроение по возрастанию дерева.'''
        left_child = left(index)
        right_child = right(index)
        if (left_child < size) and (array[left_child] > array[index]):
            largest = left_child
        else:
            largest = index
        if (right_child < size and array[right_child] > array[largest]):
            largest = right_child
        if (largest != index):
            array[largest], array[index] = array[index], array[largest]
            max_heapify(array, largest, size)

    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, index=0, size=i)
