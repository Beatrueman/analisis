from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType


def generate_3d_province(maptype: str, data: list = []):

    c = (
        Map3D()
        .add_schema(
            maptype=maptype,
            itemstyle_opts=opts.ItemStyleOpts(
                color="rgb(5,101,123)",
                opacity=1,
                border_width=0.8,
                border_color="rgb(62,215,213)",
            ),
            light_opts=opts.Map3DLightOpts(
                main_color="#fff",
                main_intensity=1.2,
                is_main_shadow=False,
                main_alpha=55,
                main_beta=10,
                ambient_intensity=0.3,
            ),
            view_control_opts=opts.Map3DViewControlOpts(
                                                        auto_rotate=True,
                                                        auto_rotate_direction='cw',
                                                        animation=True,
                                                        ),
            post_effect_opts=opts.Map3DPostEffectOpts(is_enable=True,
                                                      is_bloom_enable=True,
                                                      ),
        )
        .add(
            series_name="",
            data_pair=data,
            type_=ChartType.LINES3D,
            effect=opts.Lines3DEffectOpts(
                is_show=True,
                period=4,
                trail_width=3,
                trail_length=0.5,
                trail_color="#f00",
                trail_opacity=1,
            ),
            linestyle_opts=opts.LineStyleOpts(is_show=True, color="#fff", opacity=0),
        )
    )

    html_path = f"fe/template/static/province/{maptype}.html"
    c.render(html_path)
    #return c.render_embed()
    return html_path
    #c.render("map.html")

    #return c.render("fe/template/static/province/{}.html".format(maptype))

#generate_3d_province('陕西')