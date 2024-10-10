from pyecharts import options as opts
from pyecharts.charts import Map
from loader import get_hiv_data, year
import  sys

year = int(sys.argv[1]) if len(sys.argv) > 1 else 2020
hiv_data = get_hiv_data(year)

cases = hiv_data.get_cases()
death = hiv_data.get_death()


c = (
    Map(opts.InitOpts(width='427px', height='350px'))
    .add("发病数（单位：人）", [list(z) for z in zip(cases.keys(), cases.values())], "china", is_map_symbol_show=False)
    .add("死亡数（单位：人）", [list(z) for z in zip(death.keys(), death.values())], "china", is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国艾滋病分布情况", is_show=False),
        visualmap_opts=opts.VisualMapOpts(
                                          textstyle_opts=opts.TextStyleOpts(color="aliceblue"),
                                          is_piecewise=True,
                                          pieces=[
                                              {'min':10000, 'color':'#7f1818'},
                                              {'min':5000, 'max':10000},
                                              {'min':2000, 'max':5000},
                                              {'min':1000, 'max':2000},
                                              {"min":500,'max':1000},
                                              {'max': 500},
                                          ],
                                          ),
    legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color='aliceblue')),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    # .render("fe/template/static/visualmap.html")
)

# 获取随机生成的图表 ID
chart_id = c.chart_id

# 添加 JS 事件监听函数，使用动态的 chart_id
c.add_js_funcs(f"""
    var chart_{chart_id} = echarts.init(document.getElementById('{chart_id}'), 'white', {{renderer: 'canvas'}});
    chart_{chart_id}.on('click', function (params) {{
        if (params.seriesName === '发病数（单位：人）' || params.seriesName === '死亡数（单位：人）') {{
            // 省份名称获取
            var province = params.name;
            console.log(params);

            // 向父窗口发送消息
            window.parent.postMessage({{ type: 'provinceClick', province: province }}, '*');
        }}
    }});
    """)


# 渲染图表
c.render("fe/template/static/visualmap.html")

