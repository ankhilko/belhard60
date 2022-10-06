# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument(
#     '-p', '--port', help='PORT'
# )
# args = parser.parse_args()
# print(args)

import logging

logging.basicConfig(
    filename='log.log',
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
)


try:
    8 / 0
except ZeroDivisionError as e:
    logging.error(e)


import re

pattern1 = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") # for full match
pattern2 = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)") # for find all
print(pattern1.fullmatch("info@min.con"))
print(pattern2.findall("hagsdjhasf asfinfo@min.conasd asf asf asf"))
