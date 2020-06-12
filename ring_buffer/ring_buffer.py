class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.i_count = 0
        self.buff = [None]*capacity

    def append(self, item):
        self.buff[self.i_count] = item
        self.i_count += 1
        if self.i_count == self.capacity:
            self.i_count = 0

    def get(self):
        return [item for item in self.buff if item != None]