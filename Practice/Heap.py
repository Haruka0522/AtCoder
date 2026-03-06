from abc import ABC, abstractmethod


class Heap(ABC):
    def __init__(self):
        self.array = []

    def push(self, v) -> None:
        self.array.append(v)
        self._sift_up(len(self.array) - 1)

    def pop(self) -> int:
        min_value = self.array[0]
        matsubi = self.array.pop()
        if len(self.array) > 0:
            self.array[0] = matsubi
            self._sift_down(0)

        return min_value

    def top(self) -> int:
        return self.array[0]

    @abstractmethod
    def _sift_up(self, i) -> None:
        pass

    @abstractmethod
    def _sift_down(self, i) -> None:
        pass

    def __repr__(self):
        return f"[{', '.join(list(map(str, self.array)))}]"


class MinHeap(Heap):
    def _sift_up(self, i) -> None:
        while i > 0:
            parent = (i - 1) // 2
            value_i = self.array[i]
            value_parent = self.array[parent]
            if value_i < value_parent:
                self.array[parent] = value_i
                self.array[i] = value_parent
                i = parent
            else:
                break

    def _sift_down(self, i) -> None:
        while True:
            left = i * 2 + 1
            right = i * 2 + 2

            if left >= len(self.array):
                break

            if (len(self.array) == right) or (self.array[left] < self.array[right]):
                small = left
            else:
                small = right

            value_i = self.array[i]
            value_small = self.array[small]
            if value_i > value_small:
                self.array[i] = value_small
                self.array[small] = value_i
                i = small
            else:
                break


if __name__ == '__main__':
    min_heap = MinHeap()
    for i in [5, 2, 7, 1]:
        min_heap.push(i)

    print(min_heap)
    print(min_heap.top())
