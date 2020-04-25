import openpyxl
from wordcloud import WordCloud

# 读取数据
wb = openpyxl.load_workbook('data.xlsx')
# 获取工作表
ws =wb['国内疫情']

# 国内疫情数据
frequency_in = {}
for row in ws.values:
    # 去除表头
    if row[0] == '省份':
        pass
    else:
        # 将省份和累计确诊数关联 float转换为浮点型
        frequency_in[row[0]] = float(row[1])

# 海外疫情数据
frequency_out = {}
# 获取表名
sheet_name = wb.sheetnames
for each in sheet_name:
    if '洲' in each:
        ws = wb[each]
        for row in ws.values:
            if row[0] =='国家':
                pass
            else:
                # 写入字典
                frequency_out[row[0]] = float(row[1])


# 创建生成词云方法
def generate_pic(frequency, name):
    # font_path 字体路径 解决不显示中文
    wordcloud = WordCloud(font_path='msyh.ttc',
                          width=1920,
                          height=1080)
    # 根据确诊病例生成词云
    wordcloud.generate_from_frequencies(frequency)
    wordcloud.to_file('%s.png'%(name))
    print("ok!")


generate_pic(frequency_in, "国内疫情词云")
generate_pic(frequency_out, "世界疫情词云")
