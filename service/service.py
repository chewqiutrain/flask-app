import time 
import logging
import sys

log = logging.getLogger("MyService")
format = '[%(asctime)s - %(name)s - %(levelname)s]: %(message)s'
formatter = logging.Formatter(format)
logging.basicConfig(filename='logs/service.log', level=logging.DEBUG, format=format)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

log.addHandler(handler)


class Service(object):
    def __init__(self) -> None:
        super().__init__()
    
    def call_database(self, upid: int, seconds: int): 
        log.info(f"UPID: {upid} | Simulating call to database, sleeping for {seconds} seconds.")
        time.sleep(seconds)
        log.info(f"UPID: {upid} | Returned result from database after {seconds} seconds")
        return seconds

    def do_quick(self):
        upid = 2 
        sleep = 1 
        res = self.call_database(upid, sleep)
        return res

    def do_slow(self):
        upid = 3
        sleep = 4
        res = self.call_database(upid, sleep)
        return res
