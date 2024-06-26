# Python 学习项目

这是一个用于学习 Python 编程语言的项目，旨在帮助初学者掌握 Python 的基础知识和编程技能。

## 项目简介

该项目包含了一系列的学习资源、示例代码和练习，涵盖了 Python 的各个方面，包括但不限于：

- 基本语法
- 数据类型
- 控制流程
- 函数和模块
- 文件操作
- 异常处理
- 面向对象编程（OOP）
- 网络编程
- 数据库操作

## 学习资源

在这个项目中，你将找到以下学习资源：

- `examples/` 目录：包含了各种示例代码，涵盖了 Python 不同方面的使用方法。
- `exercises/` 目录：包含了练习题目，帮助你巩固所学知识。
- `tutorials/` 目录：包含了针对特定主题的教程和说明文档，帮助你深入理解 Python 的某些方面。

## python 版本

- 版本: python-3.12.2
- 网址: https://www.python.org/downloads/
- 下载链接: https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe

## flask 框架

- 安装 `pip install Flask`
- 清华镜像 `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Flask`
- 中文文档 https://dormousehole.readthedocs.io/en/latest/index.html

## pyinstaller 打包工具

- 安装 PyInstaller: `pip install pyinstaller`
- 清华镜像 `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller`
- 使用 PyInstaller 打包 Flask 应用: `pyinstaller app.py`
    - 其中 app.py 是启动你的 Flask 应用的 Python 脚本。PyInstaller 会分析这个脚本以及其导入的所有模块，并创建一个包含所有必要文件的分发包。


- 语法

| 参数                                  | 解释                                  |
|-------------------------------------|-------------------------------------|
| -F                                  | 所有依赖项打包到单一可执行文件                     |
| -w                                  | 使用 Windows 子系统，不显示命令行窗口（仅限 Windows） |
| -c                                  | 创建控制台应用程序，显示命令行窗口（仅限 Windows）       |
| -n <name>                           | 指定生成的可执行文件的名称                       |
| -i <icon.ico>                       | 指定生成的可执行文件的图标文件                     |
| --add-data <SRC;DEST or SRC:DEST>   | 添加额外的文件或目录到可执行文件中                   |
| --add-binary <SRC;DEST or SRC:DEST> | 添加二进制文件到可执行文件中                      |
| -p <path>                           | 添加搜索路径，查找依赖项                        |
| --hidden-import <module>            | 强制导入指定的模块                           |
| --additional-hooks-dir <path>       | 添加额外的钩子目录                           |

## pip install flask-cors 跨域请求

- 安装   `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask-cors`

## 使用 Waitress 在 Windows 上运行 Flask 应用

- 安装 `pip install waitress`
- 运行 `waitress-serve --listen=*:8880 app:app`
- 暂时不用