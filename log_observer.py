from abc import ABC, abstractmethod

class LogObserver(ABC):
    @abstractmethod
    def add_message(self, message, level):
        pass


class FileLogObserver(LogObserver):
    def add_message(self, message, level):
        log_data = {"message": message, "level": level.value}
        print("Adding log to file", log_data)



class StdOutLogObserver(LogObserver):
    def add_message(self, message, level):
        log_data = {"message": message, "level": level.value}
        print("Adding log to Stdout", log_data)


class LogStashLogObserver(LogObserver):
    def add_message(self, message, level):
        log_data = {"message": message, "level": level.value}
        print("Adding log to logstash", log_data)

    