from configparser import ConfigParser
from common.handle_path import conf_dir
import os
class HandleConfig(ConfigParser):
    def __init__(self,config_file):
        super().__init__()
        self.read(config_file,encoding="utf-8")



#创建一个实例
conf=HandleConfig(os.path.join(conf_dir,"conf.ini"))

# if __name__ == '__main__':
#     name = conf.get("logging","log_name")
#     print(name)

