import os
from loguru import logger


path = os.path.dirname(os.path.realpath(__file__))

logger.add(f'{path}/log/log.log', 
           format= '{time} {level} {message}', 
           level='DEBUG', 
           serialize=False, 
           rotation='1 month', 
           compression='zip')