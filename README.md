# python-color-logger
Beautify the logger module with color. Add success level to your logs.

To initialize color,  logger import colorlogger.py

```
from colorlogger.py import *
logger = get_logger(__name__)

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```
<img src=https://github.com/chandrasekar-r/python-color-logger/blob/master/Screenshot%202020-09-23%20at%209.36.56%20PM.png>
