import os
from loguru import logger

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

path = os.path.dirname(os.path.realpath(__file__))

logger.add(f'{path}/log/log.log', 
           format= '{time} {level} {message}', 
           level='DEBUG', 
           serialize=False, 
           rotation='1 month', 
           compression='zip')