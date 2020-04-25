import data_more
import data_get


datas = data_get.Get_data()
# 爬取数据并保存
datas.get_data()
# 更新时间
update_time = datas.get_time()
# 解析数据
datas.parse_data()

# 生成中国疫情地图
data_more.china_map(update_time)
# 生成城市疫情地图
data_more.province_map(update_time)