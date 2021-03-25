class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        if len(self.queue) == self.size :
            del self.queue[0]  # FIFO
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)
