import unittest
import os
from jsonpath import jsonpath
import requests
from common.handle_excel import HandleExcel
from common.handle_path import datas_dir
from common.handle_config import conf
from unittestreport import ddt, list_data
from common.handle_log import log


@ddt
class TestCase(unittest.TestCase):
    excel = HandleExcel(os.path.join(datas_dir, 'test_excel.xlsx'), "query")
    cases = excel.data_read()
    url = conf.get("evn", "base_url")
    """获取token'"""

    @classmethod
    def setUpClass(cls):
        url = conf.get("evn", "base_url") + "/login"
        headers = {"Content-Type": "application/json", "charset": "UTF-8"}
        # method="POST"
        parms = {"username": conf.get("test_data", "username"), "password": conf.get("test_data", "password")}
        response = requests.post(url=url, headers=headers, json=parms)
        res = response.json()
        token = jsonpath(res, "$..token")[0]
        # print(token)
        # 将token保存至请求头中
        headers["Authorization"] = "Bearer " + token
        # 将其设置为类属性方面调用
        cls.headers = headers

    @list_data(cases)
    def test_query(self, item):
        # 准备测试数据
        url = self.url + item["url"]
        method = item["method"].lower()
        parms = eval(item["data"])
        excepted = eval(item["excepted"])
        # 调用接口获取实际结果
        response = requests.request(method=method, url=url, json=parms, headers=self.headers)
        res = response.json()
        # 断言
        try:
            self.assertEqual(excepted["code"], res["code"])
            self.assertEqual(excepted["msg"], res["msg"])
        except AssertionError as e:
            log.error("测试用例--【{}】--执行不通过".format(item["title"]))
            log.error(e)
            raise e

        else:
            log.info("测试用例--【{}】--执行通过".format(item["title"]))
