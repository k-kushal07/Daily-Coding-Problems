class LogData:
    def __init__(self,size):
        self.maxSize = size
        self.circularBuffer = [None] * size
        self.index = 0

    def record(self,orderId):
        self.circularBuffer[self.index] = orderId
        self.index = (self.index + 1) % self.maxSize

    def getLast(self,i):
        return self.circularBuffer[(self.index - i + self.maxSize)% self.maxSize]


data = LogData(5) 

data.record(5)
data.record(4)
data.record(6)
data.record(9)
data.record(12)
data.record(90)
data.record(120)

print(data.getLast(3))
