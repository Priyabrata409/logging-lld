from log_observer import LogObserver

class LogSinkSubject:
    def __init__(self):
        self.observers: list[LogObserver] =[]

    def add_observer(self, log_observer):
        self.observers.append(log_observer)

    def notify_observers(self, message, level):
        for observer in self.observers:
            observer.add_message(message, level)
