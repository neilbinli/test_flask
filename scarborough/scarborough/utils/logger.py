import os
import getpass
import logging
import logging.handlers
import sys

try:
    is_log_to_console = True
    is_log_to_file = True

except Exception as e:
    logging.error('config does not valid. %s' % str(e))
    sys.exit(0)

LOGPATH = 'scarboroughlog'


def config_logging(filename, log_path='%s/%s'%(os.path.expanduser('~'), LOGPATH), to_console=True, level=logging.INFO):
    """
    @ cast logger files into ~/kolalog/ folder
    """
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logger = logging.getLogger()
    logger.handlers = []
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s  -->  %(levelname)s  -->  %(name)s:%(lineno)d  -->  %(message)s')
    r = logging.handlers.RotatingFileHandler(log_path+'/'+filename+".log", maxBytes=1E8, backupCount=5)
    r.setLevel(level)
    r.setFormatter(formatter)
    logger.addHandler(r)
    logging.basicConfig(filename=log_path+'/'+filename+".log", level=level, format=format)
    if to_console:
        console = logging.StreamHandler()
        console.setLevel(level)
        console.setFormatter(formatter)
        logger.addHandler(console)


class Filter(logging.Filter):

    def filter(self, record):
        if record.levelno >= 40 and str(record.name) != 'wx':
            print(getpass.getuser() + str(record.name) + ":" + str(record.lineno) + "-->" + str(record.msg))
        if record.name.startswith("apscheduler") or record.name.startswith("Rx"):
            return False
        else:
            return True


