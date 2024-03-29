from flask import Blueprint, request, jsonify
import os
import base64
import binascii

file_bp = Blueprint('file_bp', __name__)


@file_bp.route('/write', methods=['POST'])
def index():
    # 获取请求参数
    # filename = request.args.get('filename')
    # file_base64 = request.args.get('file_base64')  file_base64不能携带头部

    # print(request.form)
    # 获取 POST 请求的参数
    filename = request.form.get('filename')
    file_base64 = request.form.get('file_base64')

    # print(filename)
    # print(file_base64)

    # 验证参数
    if not (filename and file_base64):
        return jsonify({'error': '参数不完整'})

    # 验证是否包含头部
    if file_base64.startswith('data:'):
        # 查找逗号位置，逗号后即为Base64编码部分
        comma_index = file_base64.find(',')
        if comma_index != -1:
            file_base64 = file_base64[comma_index + 1:]

    # 解码 base64 数据
    try:
        file_content = base64.b64decode(file_base64)
    except binascii.Error:
        return jsonify({'error': '文件内容不是有效的 Base64 编码'})
    except TypeError:
        return jsonify({'error': '文件内容不是字符串类型'})
    except Exception as e:
        return jsonify({'error': '文件内容解码失败: ' + str(e)})

    # 获取当前用户的桌面路径
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    # 构建文件保存文件夹
    file_dir = os.path.join(desktop_path, 'develop/files')

    # 构建文件保存路径
    file_path = os.path.join(file_dir, filename)

    # 写入文件
    try:
        # 创建的目录路径 exist_ok=True 表示如果目录已经存在，不会抛出异常，而是忽略这个操作。
        os.makedirs(file_dir, exist_ok=True)
        # 写入文件内容
        with open(file_path, 'wb') as f:
            f.write(file_content)
            f.close()
    except PermissionError:
        return jsonify({'error': '没有权限写入文件'})
    except Exception as e:
        return jsonify({'error': f'文件写入失败: {str(e)}'})

    # 返回文件路径
    file_url = 'develop/files/' + filename
    print(file_url)
    return jsonify({'file_path': file_url})
