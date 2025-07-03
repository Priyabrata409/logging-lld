from typing import Optional

from log_manager import LogManager
from constants import LogLevel

class Logger:
    def __init__(self, log_destintion: Optional[list[str]] = None):
        self.logger_chain = LogManager.create_chain_logger()
        self.log_sink_subject = LogManager.get_log_sink_subject(log_destintion)

    __logger = None
    @staticmethod
    def get_logger(log_destintion: Optional[list[str]] = None):
        if Logger.__logger is None:
            Logger.__logger = Logger(log_destintion)
        return Logger.__logger
    
    def debug(self, message: str):
        self.logger_chain.log_message(message, LogLevel.DEBUG, self.log_sink_subject)

    def info(self, message: str):
        self.logger_chain.log_message(message, LogLevel.INFO ,self.log_sink_subject)

    def warning(self, message: str):
        self.logger_chain.log_message(message, LogLevel.WARNING, self.log_sink_subject)

    def error(self, message: str):
        self.logger_chain.log_message(message, LogLevel.ERROR ,self.log_sink_subject)




