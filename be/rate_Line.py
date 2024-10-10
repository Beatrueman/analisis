import pyecharts.options as opts
from pyecharts.charts import Line
from preprocess import HIVData

# 存放10年全国的发病率与死亡率
rates = []

for i in range(2010, 2021):
    path = r'data/全国艾滋病数据分地区/{}.xlsx'.format(i)
    data = HIVData(path)
    rate = [i] + data.get_rate()
    rates.append(rate)

# 提取年份、发病率和死亡率
# 注意数据需要是字符串形式
years = [str(year) for year, _, _ in rates]
cases_rates = [str(cases) for _, cases, _ in rates]
death_rates = [str(death) for _, _, death in rates]

c = (
    Line(opts.InitOpts(width='100%', height='280%'))
    .add_xaxis(years)
    .add_yaxis(
        "发病率",
        cases_rates,
        color='yellow',
        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        is_smooth=True,
    )
    .add_yaxis(
        "死亡率",
        death_rates,
        color='red',
        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        is_smooth=True,
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="全国艾滋病发病率/死亡率走势图", is_show=False),
                     yaxis_opts=opts.AxisOpts(is_show=True,
                                              name='单位:1/10万',
                                              axislabel_opts=opts.LabelOpts(color="aliceblue"),  # 修改坐标轴标签颜色
                                              axisline_opts=opts.AxisLineOpts(
                                                  linestyle_opts=opts.LineStyleOpts(color="aliceblue")),  # 图例颜色
                                              ),
                     xaxis_opts=opts.AxisOpts(is_show=True,
                                              name='年份',
                                              axislabel_opts=opts.LabelOpts(color="aliceblue"),  # 修改坐标轴标签颜色
                                              axisline_opts=opts.AxisLineOpts(
                                                  linestyle_opts=opts.LineStyleOpts(color="aliceblue")),
                                              ),
                    legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color='aliceblue')),

                     )
    .render("../fe/static/line.html")
)
