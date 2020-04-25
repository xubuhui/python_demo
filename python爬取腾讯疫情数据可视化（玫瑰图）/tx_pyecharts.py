import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# 读入数据, nrows数据行数
df = pd.read_csv('data.csv',nrows=30)
# 降序操作
df.sort_values(by='确诊病例', ascending=False, inplace=True)
# 提取数据
area = df['国家和地区'].values.tolist()
num = df['确诊病例'].values.tolist()

# 自定义颜色
color_series = [  '#D02C2A', '#D44C2D', '#F57A34', '#FA8F2F', '#D99D21',
                '#CF7B25', '#CF7B25', '#CF7B25','#FAE927', '#E9E416', '#C9DA36', '#9ECB3C', '#6DBC49',
                '#37B44E', '#3DBA78', '#14ADCF', '#209AC9', '#1E91CA',
                '#2C6BA0', '#2B55A1', '#2D3D8E', '#44388E', '#6A368B'
                 '#7D3990', '#A63F98', '#C31C88', '#D52178', '#D5225B',
              ]
# 实例化Pie类
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='700px'))
# 设置颜色
pie1.set_colors(color_series)
# 添加数据，设置饼图的半径，是否展示成南丁格尔图
pie1.add("", [(a,b) for a,b in zip(area, num)],
         radius=["40%", "100%"],
         center=["50%", "65%"],
         rosetype="radius"
         )
# 设置全局配置项
pie1.set_global_opts(title_opts=opts.TitleOpts(title='南丁格尔疫情图'),
                     legend_opts=opts.LegendOpts(is_show=False),
                     )
# 设置系列配置项
pie1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="top", font_size=12,
                                               formatter="{b}:累计确诊{c}例", font_style="italic",
                                               font_weight="bold", font_family="Microsoft YaHei"
                                               ),
                     )
# 生成html文档
pie1.render('南丁格尔疫情图.html')
print("构建成功")
