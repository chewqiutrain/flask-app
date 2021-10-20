from service.service import Service 

import logging
import sys
import random
import redis 

log = logging.getLogger("myapp")
format = '[%(asctime)s - %(name)s - %(levelname)s]: %(message)s'
formatter = logging.Formatter(format)
logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format=format)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

log.addHandler(handler)



def main():
    # print("in main")
    # s = log.getEffectiveLevel()
    # print(s)
    # log.debug("debug")
    # log.error("error")
    # log.info("info")
    # s = Service()
    # r = s.call_database(upid=1, seconds=2)
    # log.info(f"{r}")
    # x = random.seed(2)
    # i = random.choice([1,2,3,4,5])
    # print(i)
    # print([i for i in range(0,10)])
    r = redis.Redis(host="localhost", port=6379)
    capitals_dict = {
        "Australia": "Canberra",
        "China": "Beijing",
        "Japan": "Tokyo",
        "Singapore": "Singapore"
    }
    r.mset(capitals_dict)

    cap_japan = r.get("Japan").decode('utf-8')
    print(cap_japan)

main()