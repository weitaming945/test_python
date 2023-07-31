import unittest
from common.handle_path import report_dir, testcase_dir
from unittestreport import TestRunner


# class Testrun:
#     def main(self):
#         suit = unittest.defaultTestLoader.discover(r"C:\Users\yuemia\PycharmProjects\test_test\datas")
#         runner = TestRunner(suit,filename="py31.html",report_dir=report_dir)
#         runner.run()
#
#         runner.send_email(host="smtp.qq.com",
#                           port=465,
#                           user="1067263986@qq.com",
#                           #授权码
#                           password="oibhmlidtdmabdjc",
#                           #多个使用列表：[]
#                           to_addrs="1067263986@qq.com",
#                           is_file=True)

class RunTest:
    def main(self):
        suite = unittest.defaultTestLoader.discover(testcase_dir)
        runner = TestRunner(suite, report_dir=report_dir)
        runner.run()

        # # 通过邮件发送至相关人员邮箱
        runner.send_email(host="smtp.qq.com",
                          port=465,
                          user="1067263986@qq.com",
                          # 授权码
                          password="oibhmlidtdmabdjc",
                          # 多个使用列表：[]
                          to_addrs="1067263986@qq.com",
                          is_file=True)


if __name__ == '__main__':
    run =RunTest()
    run.main()
