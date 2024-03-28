from flask import Flask
from flask_cors import CORS

from routers.index import index_bp
from routers.file import file_bp

app = Flask(__name__)
CORS(app)

# 主页
app.register_blueprint(index_bp, url_prefix='/index_bp')
# 操作文件
app.register_blueprint(file_bp, url_prefix='/file_bp')


# 首先我们导入了 Flask 类。该类的实例将会成为我们的 WSGI 应用。
#
# 接着我们创建一个该类的实例。第一个参数是应用模块或者包的名称。 __name__ 是一个适用于大多数情况的快捷方式。有了这个参数， Flask 才能知道在哪里可以找到模板和静态文件等东西。
#
# 然后我们使用 route() 装饰器来告诉 Flask 触发函 数的 URL 。
#
# 函数返回需要在用户浏览器中显示的信息。默认的内容类型是 HTML ，因此 字符串中的 HTML 会被浏览器渲染。

# 对错误路径统一处理
@app.route('/<path:path>')
def catch_all(path): return '不存在的路径'


#
if __name__ == '__main__':
    app.run('0.0.0.0', 8880)

# request.method: 获取请求方法，例如 'GET'、'POST' 等。
# request.args: 获取查询参数，返回一个字典。
# request.form: 获取表单数据，返回一个字典。
# request.json: 获取 JSON 数据，返回一个字典。
# request.headers: 获取请求头，返回一个字典。
# request.remote_addr: 获取客户端的 IP 地址
