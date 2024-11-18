class Logger:
    def __init__(self, next_logger = None):
        self.next_logger = next_logger

    def set_next(self, logger):
        self.next_logger = logger
        return logger
    
    def handler(self, level, message):
        if self.next_logger:
            return self.next_logger.handle(level, message)
        return None
    
class InfoLogger(Logger):
    def handle(self, level, message):
        if level == "INFO":
            return f"INFO : {message}"
        
        return super().handler(level, message)
    

class WarningLogger(Logger):
    def handle(self, level, message):
        if level == "WARNING":
            return f"WARNING : {message}"
        
        return super().handler(level, message)
    
class ErrorLogger(Logger):
    def handle(self, level, message):
        if level == "ERROR":
            return f"ERROR : {message}"
        
        return super().handler(level, message)
    

info_logger = InfoLogger()
warning_logger = WarningLogger()
error_logger = ErrorLogger()

info_logger.set_next(warning_logger).set_next(error_logger)

log_messages = [
    ("INFO", "This is an info message."),
    ("WARNING", "This is a warning message."),
    ("ERROR", "This is an error message."),
    ("DEBUG", "This is a debug message.")  # No handler for DEBUG
]

for level, message in log_messages:
    result = info_logger.handle(level, message)
    if result:
        print(result)
    else:
        print(f"No handler could process the {level} message: {message}")