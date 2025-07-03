from log_observer import FileLogObserver, StdOutLogObserver, LogStashLogObserver
from log_sink_subject import LogSinkSubject
from log_handler import InfoLogger, DebugLogger, WarningLogger, ErrorLogger, LogHandler


class LogManager:
    @staticmethod
    def create_chain_logger() -> LogHandler:
        debug_logger = DebugLogger()
        info_logger = InfoLogger()
        info_logger.set_next_logger(debug_logger)
        warning_logger = WarningLogger()
        warning_logger.set_next_logger(info_logger)
        error_logger = ErrorLogger()
        error_logger.set_next_logger(warning_logger)
        return error_logger
    

    @staticmethod
    def get_log_sink_subject(log_destinations: list[str] = None) -> LogSinkSubject:
        log_sink = LogSinkSubject()
        if log_destinations is None:
            log_destinations = ["stdout"]
        for log_dest in log_destinations:
            if log_dest == "stdout":
                log_sink.add_observer(StdOutLogObserver())
            if log_dest == "file":
                log_sink.add_observer(FileLogObserver())
            if log_dest == "log_stash":
                log_sink.add_observer(LogStashLogObserver())

        return log_sink

