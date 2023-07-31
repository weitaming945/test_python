import unittest

import os
import requests
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import datas_dir
from common.handle_config import conf
from common.handle_log import log


@ddt
class TsetCase(unittest.TestCase):
    excel = HandleExcel(os.path.join(datas_dir, 'test_excel.xlsx'), "login")
    cases = excel.data_read()
    url = conf.get("evn", "base_url")

    @list_data(cases)
    def test_login(self, item):
        # 请求接口
        url = self.url + item["url"]
        # 请求参数
        parms = eval(item["data"])
        # 请求头
        headers = {"Content-Type": "application/json", "charset": "UTF-8"}
        # 请求方法
        method = item["method"].lower()
        # 预期结果
        excepted = eval(item["excepted"])
        # 调用接口获取实际结果
        response = requests.request(method=method, url=url, json=parms, headers=headers)
        res = response.json()
        try:
            self.assertEqual(excepted["code"], res["code"])
            self.assertEqual(excepted["msg"], res["msg"])
        except AssertionError as e:
            # self.excel.data_write(row=row, column=5, value="NO")
            log.error("[{}]用例执行不通过".format(item["title"]))
            log.error(e)
            # log_test.exception(e)
            raise e
        else:
            # self.excel.data_write(row=row, column=5, value="Yes")
            log.info("[{}]执行通过".format(item["title"]))
# import unittest
# import os
# import requests
# from unittestreport import ddt, list_data
# from common.handle_excel import HandleExcel
# from common.handle_path import datas_dir
# from common.handle_config import conf
# from common.handle_log import log
#
#
# @ddt
# class TestCase(unittest.TestCase):
#     excel = HandleExcel(os.path.join(datas_dir, "test_excel.xlsx"), "login")
#     cases = excel.data_read()
#     base_url = conf.get("evn", "base_url")
#     #获取请求头字符串转化字典
#     # headers = eval(conf.get("evn", "headers"))
#
#     @list_data(cases)
#     def test_func(self, item):
#         # 准备数据
#         # 接口地址、请求头、请求方法，预期结果
#         url = self.base_url + item["url"]
#         # 获取请求参数、
#         parms = eval(item["data"])
#         # 获取请求方法,并将其转化为小写
#         method = item["method"].lower()
#         #请求头
#         headers={"Content-Type":"application/json","charset":"UTF-8"}
#         # 预期结果
#         excepted = eval(item["excepted"])
#         # 获取实际结果
#         response=requests.request(method, url, json=parms, headers=headers)
#         res=response.json()
#         # 断言
#         try:
#             #一个一个断言
#             self.assertEqual(excepted["code"],res["code"])
#             self.assertEqual(excepted["msg"],res["msg"])
#             #调用封装的方法进行断言
#             # self.assertdictin(excepted,res)
#         except AssertionError as e:
#             log.error("用例---【{}】--执行失败".format(item["title"]))
#             log.error(e)
#             raise e
#         else:
#             log.info("用例---【{}】--执行通过".format(item["title"]))

# 成员断言==》封装方法

# def assertdictin(self, excepted, res):
#     for k, v in excepted.items():
#         if res.get(k) == v:
#             pass
#         else:
#             raise AssertionError("{}[k,v]not in {}".format(excepted, res))
