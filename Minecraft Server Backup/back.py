import shutil
import zipfile
import os
import datetime

# 定义Minecraft服务器文件夹和备份目标文件夹
minecraft_dir = os.path.abspath('.')  # 获取当前目录的绝对路径作为Minecraft服务器文件夹
backup_dir = os.path.join(minecraft_dir, 'backup')  # 在Minecraft服务器文件夹中创建备份目标文件夹

# 创建一个带有当前日期时间的文件夹名作为备份文件夹
backup_folder = os.path.join(backup_dir, 'backup_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(backup_folder)

# 要备份的文件夹列表
folders_to_backup = ['world', 'world_nether', 'world_the_end']

# 将这3个文件夹的内容打包成一个.zip文件
zip_filename = os.path.join(backup_folder, 'minecraft_backup.zip')
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for folder in folders_to_backup:
        folder_path = os.path.join(minecraft_dir, folder)
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, minecraft_dir)
                zipf.write(file_path, arcname)

print('备份文件已创建:', zip_filename)
