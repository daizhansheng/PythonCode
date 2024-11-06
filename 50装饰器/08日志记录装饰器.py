
import logging
from syslog import LOG_INFO

logging.basicConfig(level=LOG_INFO)
def create_log(func):
    def wrapper(*args,**kwargs):
        logging.info(f"this is log info,{func.__name__},*args = {args},**kwargs={kwargs}")
        return func(*args,**kwargs)
    return wrapper

@create_log
def log_info(i):
    print(f"这是调试时候的日志信息,{i}")

log_info("调试信息")

