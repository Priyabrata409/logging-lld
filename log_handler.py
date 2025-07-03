from abc import ABC, abstractmethod
from constants import LogLevel


class LogHandler(ABC):
    def __init__(self):
        self.next_logger = None
    def set_next_logger(self, next_logger):
        self.next_logger = next_logger
    @abstractmethod
    def log_message(self, message, level: LogLevel,  log_sink_subject):
        pass



class DebugLogger(LogHandler):      
    def log_message(self, message, level,  log_sink_subject):
        if level == LogLevel.DEBUG:
            log_sink_subject.notify_observers(message, level)
        else:
            self.next_logger.log_message(message, level, log_sink_subject)


class InfoLogger(LogHandler):      
    def log_message(self, message, level,  log_sink_subject):
        if level == LogLevel.INFO:
            log_sink_subject.notify_observers(message, level)
        else:
            self.next_logger.log_message(message, level, log_sink_subject)


class WarningLogger(LogHandler):      
    def log_message(self, message, level,  log_sink_subject):
        if level == LogLevel.WARNING:
            log_sink_subject.notify_observers(message, level)
        else:
            self.next_logger.log_message(message, level, log_sink_subject)

class ErrorLogger(LogHandler):      
    def log_message(self, message, level,  log_sink_subject):
        if level == LogLevel.ERROR:
            log_sink_subject.notify_observers(message, level)
        else:
            self.next_logger.log_message(message, level, log_sink_subject)


