利用python标准库中的zipfile和pathlib模块备份重要文件（以.zip格式存储）

使用方法：

1.在python脚本源文件中添加你想要备份的文件路径到importantFolders列表，将备份后存储文件的路径保存到zipFilePath。

2.然后在bat文件中找到你工程的python解释器的路径替换"D:\pycharm_project\auto_python\backUpImprotantFiles\.venv\Scripts\python.exe"，然后将bat文件所在目录的路径替换"D:\pycharm_project\auto_python\backUpImprotantFiles\buif.py"。

3.接着在环境变量中系统变量的Path中新建路径，新建的路径为bat文件所在目录的路径。

4.最后在命令行中输入buif后即可备份重要文件到指定的目录。
