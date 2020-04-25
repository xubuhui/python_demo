# 抓取王者荣耀皮肤
import requests
import pprint
import time

start_time = time.time()
# 爬虫的一般思路
# 1.分析目标网页，确定爬取的url路径
url = 'https://pvp.qq.com/web201605/js/herolist.json'
# 2.发送请求 --requests 模拟浏览器发送请求，获取相应数据
response = requests.get(url)
data = response.json()
# 格式化打印json
# pprint.pprint(data)

# 3.解析数据 --json模块:把json字符串转化成python可交互的数据类型
for data1 in data:
    cname = data1['cname']  # 英雄名
    ename = data1['ename']  # 英雄ID
    try:
        skin_name = data1['skin_name'].split('|')  # 皮肤名称
    except Exception as e:
        print(e)
    # 构建皮肤数量循环
    for skin_num in range(1, len(skin_name)+1):
        # 拼接图片url
        # 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+英雄ID值+'/'+英雄ID值+'-bigskin-'+皮肤序号+'.jpg'
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(ename)+'/'+str(ename)+'-bigskin-'+str(skin_num)+'.jpg'
        img_data = requests.get(skin_url).content  # 二进制数据提取
        # 4.保存数据 --保存在目标文件夹
        with open('img\\'+cname+'-'+skin_name[skin_num-1]+'.jpg','wb') as f:
                print('正在下载图片：', cname+'-'+skin_name[skin_num-1])
                f.write(img_data)
f.close()
end_time = time.time()
print('花费时间：',end_time-start_time)






