import logging

logger = None


def setup_logging():
    """:arg
    setup logging"""
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='logs.log',
                        filemode='w',
                        )


def set_logger(app_name):
    global logger
    logger = logging.getLogger(app_name)






