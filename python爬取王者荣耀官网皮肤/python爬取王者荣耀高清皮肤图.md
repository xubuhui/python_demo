---
title: python爬取王者荣耀高清皮肤图
author: HeZ
avatar: 'https://cdn.jsdelivr.net/gh/woshigehaoren/mycdn@1.5/img/custom/head.jpg'
authorLink: xubuhui.github.io
authorAbout: 一个可爱的人
authorDesc: 一个可爱的人
categories: 技术
comments: true
photos: >-
  https://cdn.jsdelivr.net/gh/xubuhui/mycdn@2.8/img/me/dm3.jpg
date: 2020-04-21 20:52:25
tags: 
 - python
 - 爬虫
keywords:
description: python爬取图片
---


### 关于爬虫的一些思路

首先我们打开王者荣耀官网，进入英雄资料界面

![img](https://cdn.jsdelivr.net/gh/xubuhui/mycdn@2.7/img/blog/wz1.png)

python爬取腾讯疫情数据并可视化（二）
进入一个英雄的具体介绍页面

然后f12，打开浏览器调试窗口，首先找到皮肤图片的url
![img](https://cdn.jsdelivr.net/gh/xubuhui/mycdn@2.7/img/blog/wz3.png)

分析提供图片的数据包

NetWork->XHR

![img](https://cdn.jsdelivr.net/gh/xubuhui/mycdn@2.7/img/blog/wz4.png)

### 下面是具体代码实现

```python
# 抓取王者荣耀皮肤
import requests
import pprint
import time
# 程序开始时间
start_time = time.time()
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
# 程序结束时间
end_time = time.time()
# 打印程序运行花费时间
print('花费时间：',end_time-start_time)
```