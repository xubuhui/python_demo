import json
import requests
from lxml import etree
import openpyxl

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1'
response = requests.get(url)
# print(response.text)
# 生成html对象
html = etree.HTML(response.text)
# 获取列表
r = html.xpath('//script[@type="application/json"]/text()')
# json.loads将字符串转换为python数据类型
result = json.loads(r[0])
# print(result['component'][0]['caseList'])
# 创建工作簿
wb = openpyxl.Workbook()
# 创建工作表
ws = wb.active
ws.title = '国内疫情'
# 表头
ws.append(['省份','累计确诊','死亡','治愈','现有确诊','累计确诊增量'])
# 国内疫情数据
result_in = result['component'][0]['caseList']
for data_in in result_in:
    temp_list = [data_in['area'], data_in['confirmed'],data_in['died'],data_in['crued'],data_in['curConfirm'],
               data_in['confirmedRelative']
                 ]
    # 判断是否为空 如果空数据则赋值 0，0是字符串
    for i in range(len(temp_list)):
        if temp_list[i] == '':
            temp_list[i] = '0'
    ws.append(temp_list)
# 国外疫情数据
result_out = result['component'][0]['globalList']
# print(result_out)
for data_out in result_out:
    # 表名
    sheet_title = data_out['area']
    # 创建新的工作表
    ws_out = wb.create_sheet(sheet_title)
    ws_out.append(['国家','累计确诊','死亡','治愈','现有确诊','累计确诊增量'])
    # subList 具体国家疫情数据
    for sub_out in data_out['subList']:
        sub_list = [sub_out['country'], sub_out['confirmed'],sub_out['died'],sub_out['crued'],sub_out['curConfirm'],
               sub_out['confirmedRelative']]
        # 防止数据为空 如果空则 赋值0
        for i in range(len(sub_list)):
            if sub_list[i] == '':
                sub_list[i] = '0'
        ws_out.append(sub_list)
wb.save('./data.xlsx')
print("Ok")
