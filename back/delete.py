import os
import shutil


def remove_pycache_files(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir == '__pycache__':
                dir_path = os.path.join(root, dir)
                shutil.rmtree(dir_path)

        for file in files:
            if file.endswith('.pyc'):
                file_path = os.path.join(root, file)
                os.remove(file_path)


# 获取当前工作目录
current_directory = os.getcwd()

# 调用函数删除 __pycache__ 文件夹和 .pyc 文件
remove_pycache_files(current_directory)
