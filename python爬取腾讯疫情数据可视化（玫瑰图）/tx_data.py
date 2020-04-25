import requests
import json
import pandas as pd

# 分析抓包
url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
response = requests.get(url)
content = json.loads(response.text)  # json.loads 将json格式数据转换为字典
# print(content)
df = pd.DataFrame(columns=['国家和地区','确诊病例','死亡病例','治愈病例'])
# 字典类型读取到DataFrame
for i in range(len(content['data'])):
        df.loc[i+1] = [
            content['data'][i]['name'],
            content['data'][i]['confirm'],
            content['data'][i]['dead'],
            content['data'][i]['heal']]
# 保存为csv格式文件
df.to_csv('data.csv', index=0, encoding='utf-8')
print('爬取完毕')
