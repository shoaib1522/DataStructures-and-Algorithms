from process import Process
from scheduler import Scheduler

if __name__ == "__main__":
    arr = [Process(1, "notepad", 20), Process(13, "mp3player", 5), Process(4, "bcc", 30), Process(11, "explorer", 2)]
    s = Scheduler(arr, 4, 5)
    s.assignProcessor()
