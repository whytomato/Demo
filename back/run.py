import os
import platform
import signal
import shutil


def cleanup(signal, frame):
    # 在这里执行删除操作
    remove_pycache_files(current_directory)
    print("Cleanup completed. Exiting...")
    exit(0)


# 注册终止信号处理程序
signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)


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

os.system("python manage.py makemigrations")
os.system("python manage.py migrate")

if platform.system() != "Linux":
    os.system("python manage.py runserver")
else:
    os.system("python manage.py runserver 0.0.0.0:8000 > log.txt & \n")

print("The backend is running!")
