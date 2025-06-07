class Process:
    def __init__(self, processId, processName, processExecTime):
        self.processId = processId
        self.processName = processName
        self.processExecTime = processExecTime

    def display(self):
        print(f"Process ID: {self.processId}, Name: {self.processName}, Execution Time: {self.processExecTime}")
