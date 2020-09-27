import yaml
from utils import log


class Config(object):
    """:arg
    singleton config class"""

    __instance = None

    @staticmethod
    def __read_yaml(config_file):
        return yaml.load(open(config_file))

    def __init__(self, app_name):
        if Config.__instance:
            raise Exception("Can't create two config instances! ")
        self.__app_name = app_name
        config_path = 'config/{0}.yml'.format(app_name)
        self.__config = self.__read_yaml(config_path)
        Config.__instance = self

    def get(self, key, expected_type=int):
        if key in self.__config:
            if not isinstance(self.__config[key], expected_type):
                log.logger.warning("type of {0} is not expected {1} and is {2}".format(key, expected_type, type(self.__config[key])))
        else:
            log.logger.warning("no such key in config {0}".format(key))

        return self.__config.get(key, None)


