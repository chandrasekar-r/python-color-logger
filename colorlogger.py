import logging
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

COLORS = {
    'WARNING': YELLOW,
    'INFO': BLUE,
    'DEBUG': CYAN,
    'CRITICAL': YELLOW,
    'ERROR': RED,
    'RED': RED,
    'SUCCESS': GREEN,
    'YELLOW': YELLOW,
    'BLUE': BLUE,
    'MAGENTA': MAGENTA,
    'CYAN': CYAN,
    'WHITE': WHITE,
}
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


class ColorFormatter(logging.Formatter):
    """
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    is getting replaced with below line
    formatter = ColorFormatter('$COLOR%(levelname)s $RESET %(asctime)s $BOLD%(module)s$RESET $COLOR%(message)s')
    """
    def __init__(self, *args, **kwargs):
        # can't do super(...) here because Formatter is an old school class
        logging.Formatter.__init__(self, *args, **kwargs)

    def format(self, record):
        levelname = record.levelname
        color = COLOR_SEQ % (30 + COLORS[levelname])
        message = logging.Formatter.format(self, record)
        message = message.replace("$RESET", RESET_SEQ) \
            .replace("$BOLD", BOLD_SEQ) \
            .replace("$COLOR", color)
        for k, v in COLORS.items():
            message = message.replace("$" + k, COLOR_SEQ % (v + 30)) \
                .replace("$BG" + k, COLOR_SEQ % (v + 40)) \
                .replace("$BG-" + k, COLOR_SEQ % (v + 40))
        return message + RESET_SEQ


def get_logger(file_name):
    """
    :param file_name: Takes values '__all__' or any filename
    :return: logger
    """
    # set success level
    logging.SUCCESS = 25  # between WARNING and INFO
    logging.addLevelName(logging.SUCCESS, 'SUCCESS')
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)

    formatter = ColorFormatter('$COLOR%(levelname)s $RESET %(asctime)s $BOLD%(module)s$RESET $COLOR%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    setattr(logger, 'success', lambda message, *args: logger._log(logging.SUCCESS, message, args))
    return logger
