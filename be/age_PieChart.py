from pyecharts import options as opts
from pyecharts.charts import Pie
from loader import get_hiv_agegroup_data, year
import sys



# hiv_age_data = HIVAgeData(r"..\data\全国艾滋病数据分年龄\2020.xlsx")
# age_data = HIVAgeData.get_age_group(hiv_age_data)
#hiv_age_data = get_hiv_age_data(2020)

year = int(sys.argv[1]) if len(sys.argv) > 1 else 2020
age_data = get_hiv_agegroup_data(year)

data_cases = [[key, value[0]] for key, value in age_data.items()]
data_deaths = [[key, value[1]] for key, value in age_data.items()]

c = (
    Pie(opts.InitOpts(width='90%', height='280%'))
    .add(
        "发病数",
        data_cases,
        radius=["10%", "30%"],
        center=["20%", "50%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False),
        min_angle=30,
    )
    .add(
        "死亡数",
        data_deaths,
        radius=["10%", "30%"],
        center=["62%", "55%"],
        rosetype="area",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="全国按年龄艾滋病人数统计", is_show=False),
                     legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color='aliceblue')),
                     )
    .render("fe/template/static/pie_age.html")
)
