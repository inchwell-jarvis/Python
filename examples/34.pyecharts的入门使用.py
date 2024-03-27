# 引入 pyecharts
from pyecharts.charts import Line
from pyecharts.options import TooltipOpts, TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()
# 添加x，y轴的数据
line.add_xaxis(['中国', '英国', '美国'])
line.add_yaxis("GDP", [34, 23, 45])

line.set_global_opts(
    title_opts=TitleOpts(title="测试", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True),
)

# 生成图像
line.render()
