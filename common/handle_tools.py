import re
from common.handle_config import conf

class TeseData:
    id=12
    name="musen"
    age=18
    title="enen"

data='{"id":"#id#","name":"#name#","age":"#age#","title":"#title#","a":"aa"}'
def replace_data(data,cls):
    while re.search('#(.+?)#',data):
        res1=re.search('#(.+?)#',data)
        item=res1.group()
        atter=res1.group(1)
        try:
            value=getattr(cls,atter)
        except AttributeError as e:
            value=getattr(conf.get("test_data"),atter)
        data=data.replace(item,str(value))
        return data

if __name__ == '__main__':
    data=replace_data(data,TeseData)
print(data)
