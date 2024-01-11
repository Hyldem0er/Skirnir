from random import choice
import csv, sys
from loguru import logger
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")


class Proxy():

    def __init__(self, filepath):

        self.__proxies_dict = []
        self.__is_private_proxies = False
        self.__name = filepath.split('/')[-1]

        print(filepath)
        with open(filepath, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            header_row = next(csv_reader, None)
            if header_row is not None and len(header_row) == 4:
                self.__is_private_proxies = True
            if header_row is not None:
                self.__proxies_dict.append(header_row)
            for row in csv_reader:
                self.__proxies_dict.append(row)

    def get_proxy(self):
        """
        Retrieves a proxy from the list of available proxies.

        This function calls the 'retrieve_proxies_list()' function to obtain a list of proxies.
        It then randomly selects a proxy from the list using the 'choice()' function from the 'random' module.

        Returns:
            str: A randomly selected proxy from the list.

        Example:
            >>> get_proxy()
            '127.0.0.1:8080'
        """
        try:
            print(self.__proxies_dict)
            return choice(self.__proxies_dict)
        except Exception as error:
            logger.error(error)

    def is_private_proxy(self):
        return self.__is_private_proxies
    
    def get_name(self):
        return self.__name
    
    def pretty_print(self):
        print(self.__name)
        print(self.__is_private_proxies)
        print(self.__proxies_dict)