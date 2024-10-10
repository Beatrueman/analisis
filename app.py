from flask import Flask, request, jsonify, g, send_file
from flask_cors import CORS

from be import loader
import subprocess

from be.generate_3d_province import generate_3d_province

app = Flask(__name__, template_folder='fe/template', static_folder='fe/template/static')
# 允许所有来源的请求
CORS(app, resources={r"/generate_3d_map": {"origins": "http://localhost:5173"}})


@app.before_request
def before_request():
    g.year = loader.get_current_year()  # 获取当前年份


# @app.route('/')
# def index():
#     return render_template('index.html', year=g.year)

@app.route('/update_year', methods=['POST'])
def update_year():
    year = int(request.form.get('year'))
    loader.update_year(year)  # 更新 loader.py 中的 year 变量
    g.year = year
    loader.year = g.year

    # 生成对应的统计图html文件
    scripts = [
        'be/age_PieChart.py',
        'be/cases_BarChart.py',
        'be/death_BarChart.py',
        'be/map.py'
    ]

    for script in scripts:
        subprocess.run(['python3', script, str(year)])

    return jsonify({'success': True})


@app.route('/generate_3d_map')
def generate_3d_map_route():
    province = request.args.get('province')

    # 特殊省份处理
    special_provinces = {
        '内蒙古自治区': '内蒙古',
        '西藏自治区': '西藏',
        '广西壮族自治区': '广西',
        '宁夏回族自治区': '宁夏',
        '新疆维吾尔自治区': '新疆',
        '黑龙江省': '黑龙江'
    }

    if province in special_provinces:
        province = special_provinces[province]
    else:
        province = province[:2]

    generate_3d_province(province)

    return f'/static/province/{province}.html'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
