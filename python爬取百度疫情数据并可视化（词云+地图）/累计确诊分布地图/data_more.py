import json
import map_draw
import data_get

with open('data.json', 'r') as file:
    data = file.read()
    data = json.loads(data)
map = map_draw.Draw_map()


# print(data)
# 中国疫情地图数据
def china_map(update_time):
    area = []
    confirmed = []
    for each in data:
        # print(each)
        area.append(each['area'])
        confirmed.append(each['confirmed'])
    map.to_map_china(area, confirmed, update_time)


# 省份疫情地图数据
def province_map(update_time):
    for each in data:
        city = []
        confirmeds = []
        province = each['area']
        # 出现空列表是因为特别行政区
        for each_city in each['subList']:
            city.append(each_city['city'] + "市")
            confirmeds.append(each_city['confirmed'])
            map.to_map_city(city, confirmeds, province, update_time)
        if province == '上海' or '北京' or '天津' or '重庆':
            for each_city in each['subList']:
                city.append(each_city['city'])
                confirmeds.append(each_city['confirmed'])
                map.to_map_city(city, confirmeds, province, update_time)
    print("生成城市疫情地图成功")
