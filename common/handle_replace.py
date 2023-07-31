# 表示匹配边界
# 字符串边界：
import re

# s='123456789pythom1212'
# ^：表示字符串的开头（起始位置）
# res1=re.findall("^23",s)
# print(res1)
# $：表示字符串的结尾（终止位置）
# res2=re.findall("2$",s)
# print(res2)

# \b:表示单词边界,在python中的\b表示转义字符
# s1="pythonN is good java"
# res3=re.findall(r"\bpython",s1)   #r：防转义
# print(res3)
# \D：表示非单词边界
# res4=re.findall(r"python\B",s1)   #r：防转义
# print(res4)

# B表示分组
# parms='{"id":"#id#","name":"#name#","aa":"aaa"}'
# #想要提取什么，使用（）进行提取
# res=re.findall("#(.+?)#",parms)
# print(res)
#
# parms="sdfdf#user=haha-pwd=123#djhfjdhf"
# res1=re.findall(R"#user=(.+?)-pwd=(.+?)",parms)
# print(res1)
#
# #|:表示多个匹配规则,只要满足一个就可以
# s="123python456java789"
# res=re.findall("python|jva",s)
# print(res)
#
# s2="aaa@@python@aaadhdf#sjfh#aad"
# res=re.findall("#.+?#|@.+?@",s2)
# print(res)

# search:匹配并返回第一个符合规则的匹配对象
# parms = '{"id":"#id#","name":"#name#","aa":"aaa"}'
# res=re.search("#(.+?)#",parms)
# #打印出来是匹配对象
# print(res)
# #提取匹配对象中的内容
# # print(res.group())
# #提取第一个括号内第一个匹配的内容
# print(res.group(1))

import re


class TestDase:
    id = 123
    name = "haha"


s2 = '{"id":"#id#","name":"#name#"}'
while re.search("#(.+?)#", s2):
    res2 = re.search("#(.+?)#", s2)
    print(res2)
    item = res2.group()
    atter = res2.group(1)
    value = getattr(TestDase, atter)
    s2 = s2.replace(item, str(value))

print(s2)
