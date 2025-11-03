from configparser import ConfigParser

def read_config_data(category, key):

    loc = r"C:\Users\sasik\PycharmProjects\FrameworkPractice\config\config.ini"
    config = ConfigParser()
    config.read(loc)
    return config.get(category, key)