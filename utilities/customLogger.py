import logging
import inspect


class LogGen:
    @staticmethod
    def loggen():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler(
            "./Logs/automation.log", mode='a')  # a stands for append
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger
