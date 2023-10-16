from config import logger
from rich import print


@logger.catch
def main():
    print('app')


if __name__ == '__main__':
    main()