class Queue:
    def __init__(self, capacity: int) -> None:
        self._queue = []
        self._capacity = capacity

    def size(self) -> int:
        return len(self._queue)

    def push_front(self, element: any) -> None:
        temp: list = [element]
        self._queue = temp + self._queue

        if len(self._queue) > self._capacity:
            self._queue = self._queue[0 : self._capacity]

        return

    def push_back(self, element: any) -> None:
        self._queue.append(element)
        if len(self._queue) > self._capacity:
            self._queue = self._queue[
                len(self._queue) - self._capacity : len(self._queue)
            ]
        return

    def pop_back(self) -> any:
        returnValue = self._queue.pop()
        return returnValue

    def pop_front(self) -> any:
        returnValue = self._queue[0]
        self._queue = self._queue[1 : len(self._queue)]
        return returnValue

    def delete(self, index) -> None:
        self._queue = self._queue[0:index] + self._queue[index + 1 : len(self._queue)]

    def refer(self, index: int) -> any:
        return self._queue[index]

    def find(self, element) -> bool:
        if self.size() == 0:
            return False

        for dict in self._queue:
            if (
                dict["title"] == element["title"]
                or dict["mainText"] == element["mainText"]
            ):
                return True

        return False
