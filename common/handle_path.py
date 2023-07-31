import os

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#获取用例数据的文件路径

datas_dir=os.path.join(base_dir,"datas")

#获取报告的路径
report_dir=os.path.join(base_dir,"reports")

#获取日志文件的路径
logs_dir=os.path.join(base_dir,"logs")

#获取配置文件所在目录
conf_dir=os.path.join(base_dir,"conf")

#获取运行文件所在目录
testcase_dir=os.path.join(base_dir,"testcases")

