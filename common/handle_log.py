from common.handle_config import conf
from common.handle_path import logs_dir
import os
import logging
def log_test(name='name',level="DEBUG",sh_level="DEBUG",filename="log.log",fh_level="DEBUG"):
    #设置日志收集器
    log=logging.getLogger(name)
    log.setLevel(level)
    #创建输出渠道==》控制台
    sh=logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)
    #创建输出渠道==》文件
    fh=logging.FileHandler(filename,encoding='utf-8')
    fh.setLevel(fh_level)
    log.addHandler(fh)
    #设置输出格式
    formats = '%(asctime)s-[%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
    log_formats=logging.Formatter(formats)
    sh.setFormatter(log_formats)
    fh.setFormatter(log_formats)
    #返回日志收集器
    return log



# 为了避免程序中创建多个日志收集器而导致日志重复记录
# 创建日志收集器,测试方法调用时,from handle_log import my_log,可以直接使用my_log.error("内容")
# my_log = create_log()

# 调用配置文件中的内容,conf是handle_config.py中的定义的变量,导入调用
# 若要更改,直接更改配置文件中的值

# filename,传入路径加文件名

log = log_test(
                    name=conf.get("logging","name"),
                    level=conf.get("logging","level"),
                    filename=os.path.join(logs_dir,conf.get("logging","filename"))+".log",
                    sh_level=conf.get("logging","sh_level"),
                    fh_level=conf.get("logging","fh_level")
                    )
