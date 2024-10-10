from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType
from loader import get_hiv_data
import sys

# hiv_data = HIVData(r"..\data\全国艾滋病数据分地区\2020.xlsx")
year = int(sys.argv[1]) if len(sys.argv) > 1 else 2020
hiv_data = get_hiv_data(year)
location = []
values = []


top_ten_cities = hiv_data.get_top_n_cities_by_death(n=10)
for city, death in top_ten_cities:
    if city == '黑龙江省' or city == '内蒙古自治区':
        location.append(city[:3])
    location.append(city[:2])
    values.append(death)


c = (
    PictorialBar(opts.InitOpts(width='100%', height='340%'))
    .add_xaxis(location[::-1],)
    .add_yaxis(
        "",
        values[::-1],
        label_opts=opts.LabelOpts(is_show=True,
                                  position='right',
                                  font_style='italic',
                                  font_weight='bold',
                                  border_radius=5
                                  ),
        symbol_size=12,
        color='#CD2626',
        symbol_repeat="fixed",
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国艾滋病死亡数TOP10",
                                  is_show=True,
                                  pos_left='100px',
                                  title_textstyle_opts=opts.TextStyleOpts(color='aliceblue', border_radius='35px')),
        xaxis_opts=opts.AxisOpts(is_show=True,
                                 name='人',
                                 axislabel_opts = opts.LabelOpts(color="aliceblue"),  # 修改坐标轴标签颜色
                                 axisline_opts = opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="aliceblue")), # 图例颜色
                                 ),
        yaxis_opts=opts.AxisOpts(is_show=True,
                                 axislabel_opts = opts.LabelOpts(color="aliceblue"),
                                 axisline_opts = opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="aliceblue")),
                                 ),
    )
    .render("fe/template/static/bar_death.html")
)
