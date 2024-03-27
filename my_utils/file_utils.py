def print_file_info(filename):
    f = None
    try:
        f = open(filename, 'r', encoding='UTF-8')
        content = f.read()
        print(content)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()


def append_file_info(filename,data):
    f = open(filename, 'a', encoding='UTF-8')
    f.write(data)
    f.close()


if __name__ == '__main__':
    # print_file_info('C:/Users/22379/Desktop/test.txt')
    append_file_info('C:/Users/22379/Desktop/test2.txt','赵鸿飞')