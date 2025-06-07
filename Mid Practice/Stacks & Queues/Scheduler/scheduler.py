from queue import Queue
class Scheduler:
    def __init__(self, processArray, processArrayLength, timeQuantum):
        self.processArray = processArray
        self.processArrayLength = processArrayLength
        self.timeQuantum = timeQuantum
        self.queue = Queue(processArrayLength)

    def assignProcessor(self):
        for process in self.processArray:
            self.queue.enQueue(process)

        time = 0
        while not self.queue.isEmpty():
            current_process = self.queue.deQueue()
            current_process.display()
            for _ in range(self.timeQuantum):
                if current_process.processExecTime > 0:
                    current_process.processExecTime -= 1
                    time += 1
                else:
                    break
            if current_process.processExecTime <= 0:
                print(f"At time {time}, {current_process.processName} completed execution")
            else:
                self.queue.enQueue(current_process)
                print(f"At time {time}, Pausing execution of {current_process.processName}")
