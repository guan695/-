#! python3
# 将importantFolders路径的整个目录压缩到指定filesZip目录下的zip文件

import zipfile
from pathlib import Path

importantFolders = [
    "F:/电子书籍",
    "F:/截图",
    "F:/学习笔记",
    "D:/pycharm_project",
]

zipFilePath = "F:/backUp/ImpFiles.zip"

# 全局只打开一次zip文件保证每次程序执行时只覆盖一次zip文件的内容
zipFile = zipfile.ZipFile(zipFilePath, "w")

def compress_folder_to_zip(folder_path):
    """
    :param folder_path: str, provide the path of the folder to compress
    :return: None
    """
    folder_to_compress = Path(folder_path)

    folder_basename = folder_to_compress.name

    for folder, subfolders, files in folder_to_compress.walk():
        print(f"compressing {folder}")
        # 计算相对路径从而不包含多余的上级目录
        rel_folder = folder.relative_to(folder_to_compress)
        zip_folder_path = Path(folder_basename) / rel_folder
        # 在.zip文件中以相对路径的形式添加folder
        zipFile.write(folder, zip_folder_path)

        for file in files:
            # 换成绝对路径
            file = folder / file
            rel_file = file.relative_to(folder_to_compress)
            zip_file_path = Path(folder_basename) / rel_file
            zipFile.write(file, zip_file_path)

    return

for importantFolder in importantFolders:
    compress_folder_to_zip(importantFolder)

print("done")
zipFile.close()
