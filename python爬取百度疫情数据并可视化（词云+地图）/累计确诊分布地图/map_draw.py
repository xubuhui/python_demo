from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


class Draw_map():
    # 颜色RGB转换 脱离函数，不需要定义self
    def get_color(self,a,b,c):
        result = '#'+''.join(map((lambda x:"%02x" % x),(a,b,c)))
        return result.upper()

    def to_map_city(self, area, variate,province,update_time):
        pieces = [
            {"max": 99999999, "min": 1001, 'label': '>10000', 'color': self.get_color(102,2,8)},
            {"max": 9999, "min": 1000, 'label': '1000-9999', 'color':self.get_color(140,13,13)},
            {"max": 999, "min": 500, 'label': '500-999', 'color':self.get_color(204,41,41)},
            {"max": 499, "min": 100, 'label': '100-999', 'color': self.get_color(255,123,105)},
            {"max": 99, "min": 50, 'label': '50-99', 'color': self.get_color(255,170,133)},
            {"max": 49, "min": 10, 'label': '10-49', 'color':self.get_color(255,202,179)},
            {"max": 9, "min": 1, 'label': '1-9', 'color': self.get_color(255,228,217)},
            {"max": 0, "min": 0, 'label': '0', 'color': self.get_color(255,255,255)},
        ]

        c = (
            # 设置地图大小
            Map(init_opts=opts.InitOpts(width='1000px',height='880px'))
                .add("累计确诊人数", [list(z) for z in zip(area, variate)],province,is_map_symbol_show=False)
                .set_global_opts(
                title_opts=opts.TitleOpts(title="%s地区疫情地图分布"%(province),subtitle='截至%s %s省疫情分布情况'%(update_time,province)
                                          ,pos_left='center',pos_top='30px',),
                legend_opts=opts.LegendOpts(is_show=False),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True, pieces=pieces)
            )
                .render("./map/{}疫情地图.html".format(province))
        )

    def to_map_china(self, area, variate, update_time):
        # 分段
        pieces = [
            {"max": 99999999, "min": 1001, 'label': '>10000', 'color': '#8A0808'},
            {"max": 9999, "min": 1000, 'label': '1000-9999', 'color': '#B40404'},
            {"max": 999, "min": 100, 'label': '100-999', 'color': '#DF0101'},
            {"max": 99, "min": 10, 'label': '1-9', 'color': '#F5A9A9'},
            {"max": 9, "min": 1, 'label': '1-9', 'color': '#F5A9A9'},
            {"max": 0, "min": 0, 'label': '0', 'color': '#FFFFFF'},
        ]
        c = (
            Map(init_opts=opts.InitOpts(width='1000px', height='880px'))
                # zip内置函数，实现数据对应
                .add("累计确诊人数", [list(z) for z in zip(area, variate)], "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国疫情地图分布", subtitle='截至%s 中国疫情分布情况' % (update_time),
                                          pos_left='center',pos_top='30px'),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True, pieces=pieces),
            )
                .render("中国疫情地图.html")
        )
        print("生成中国疫情地图成功")

