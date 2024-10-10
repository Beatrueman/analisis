# **全国艾滋病数据可视化分析**

## 整体效果

![image-20241007005222002](https://gitee.com/beatrueman/images/raw/master/img/202410070052428.png)

![image-20241007005358077](https://gitee.com/beatrueman/images/raw/master/img/202410070053508.png)

![image-20241007010047310](https://gitee.com/beatrueman/images/raw/master/img/202410070100656.png)

![image-20241008225909478](https://gitee.com/beatrueman/images/raw/master/img/202410082259896.png)

## 技术栈

***Python***：使用*pandas*做数据处理，使用[*pyecharts*](https://pyecharts.org/#/zh-cn/intro)做数据可视化生成，使用*flask*制作接口（用于根据年份更新对应的数据）

数据来源于[公共卫生科学数据中心 (phsciencedata.cn)](https://www.phsciencedata.cn/Share/)

***HTML + CSS  + JS***：用于前端页面的渲染。

- 使用*jQuery*库实现AJAX发送请求到服务器用来更新各年份对应的数据以及生成对应省份的3D图。
- 使用*Bootstrap*库实现图片的轮播以及3D模态框的展示。

参考[10分钟在网站上增加一个AI助手](https://help.aliyun.com/zh/model-studio/use-cases/add-an-ai-assistant-to-your-website-in-10-minutes?spm=a2c4g.11186623.0.0.613365dfLQUfDC#80d3029cb9q06)，利用[阿里云百炼](https://bailian.console.aliyun.com/?spm=a2c4g.11186623.0.0.12dc65dfmbl1gr#/home)，将通义千问接入项目，提供艾滋病相关知识的科普。

### 接口介绍

`POST /update_year`

传入前端选择框中的year，根据year执行对应的生成统计图表的Python文件。

`GET /generate_3d_map`

前端通过监听鼠标点击事件，识别用户点击的哪一个省份。将省份province传入该接口，province作为参数传入生成3D图的函数，生成对应省份的3D html文件到`fe/template/static/province`

## 功能介绍

### 统计图展示

整个页面展示了五个统计图

- 饼图（Pie）：分年龄段展示本年艾滋病人数。
- 象形柱状图（PictorialBar）：展示本年艾滋病全国发病数/死亡数前十名。
- 折线图（Line）：2010-2020年全国发病率/死亡率走势图。
- 地图（Map）：展示本年艾滋病全国分布情况。
- 3D地图（Map3D）：展示每个省份的3D效果。

### 根据年份更新数据

点击年份选择框，可以更新对应年份的数据。

![image-20241008225445165](https://gitee.com/beatrueman/images/raw/master/img/202410082254625.png)

![image-20241008225503436](https://gitee.com/beatrueman/images/raw/master/img/202410082255816.png)

### 图片轮播

页面中心有三张有关艾滋病科普知识的图片进行轮播。

![image-20241008225552527](https://gitee.com/beatrueman/images/raw/master/img/202410082255702.png)

![image-20241008225603595](https://gitee.com/beatrueman/images/raw/master/img/202410082256681.png)

### AI科普顾问

点击右下角的小圆圈，可以调出AI（通义千问），用户可以与其对话，了解艾滋病的相关知识。

![image-20241008225732685](https://gitee.com/beatrueman/images/raw/master/img/202410082257072.png)

### 3D省份展示

点击全国艾滋病分布情况中的任意省份，页面会弹出对应省份的3D图。

![image-20241008225837981](https://gitee.com/beatrueman/images/raw/master/img/202410082258562.png)

## 部署

### Linux裸机部署

**环境**

- Python 3.11.2
- node v18.19.0
- Debian bookworm

先安装依赖

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

然后运行`app.py`，期间保持其一直运行（建议制作service）

```
python3 app.py
```

再进入`analysis/fe/template`，先安装依赖

```
npm install
```

最后运行程序

```
npm run dev -- --host
```

整个程序的入口为以下这些IP

![image-20241009102009641](https://gitee.com/beatrueman/images/raw/master/img/202410091020708.png)

### Docker部署

整个项目已打包为Docker镜像，并推送至仓库。

`beatrueman/analisis:1.0.0`

```
docker run -p 5173:5173 beatrueman/analisis:1.0.0
```

