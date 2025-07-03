from logger import Logger


def main():

    logger =  Logger.get_logger(["log_stash"])
    logger.info("Hii this is info message")
    logger.debug("this is debug message")
    logger.error("this is error messafge")
    logger.warning("this is warning messafge")

main()