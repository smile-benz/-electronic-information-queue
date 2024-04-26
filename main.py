#Код
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("Пациент 1")
    queue.enqueue("Пациент 2")
    queue.enqueue("Пациент 3")
    print("Текущий пациент в очереди:", queue.peek())
    discharged_patient = queue.dequeue()
    print("Выписан пациент:", discharged_patient)
    print("Очередь пуста?", queue.is_empty())
    print("Размер очереди:", queue.size())
