import requests
from lxml import etree
import json
import re


# 获取数据
class Get_data():
    # 抓取数据
    def get_data(self):
        url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1'
        response = requests.get(url)
        with open('html.txt','w') as file:
            file.write(response.text)
            print("写入txt成功")

    # 获得更新时间
    def get_time(self):
        with open('html.txt', 'r') as file:
            text = file.read()
        time = re.findall('"mapLastUpdatedTime":"(.*?)"', text)[0]
        return time

    # 解析数据
    def parse_data(self):
        with open('html.txt', 'r') as file:
            text = file.read()
        html = etree.HTML(text)
        result = html.xpath('//script[@type="application/json"]/text()')[0]
        result = json.loads(result)
        result = result['component'][0]['caseList']
        # result['component'][0]获得列表第0项 是一个字典
        # print(result['component'][0]['caseList'])
        # 字典转换为字符串
        result = json.dumps(result)
        with open('data.json', 'w') as file:
            file.write(result)
            print('写入json成功')


# data = Get_data()
# data.get_data()
# data.get_time()
# data.parse_data()
