# 通过 pip 安装第三方包
# 命令 pip install 包名
# 使用国内镜像安装命令 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
# numpy
import numpy


from my_utils import file_utils
file_utils.append_file_info('C:/Users/22379/Desktop/test3.txt','赵鸿飞2')
file_utils.print_file_info('C:/Users/22379/Desktop/test3.txt')