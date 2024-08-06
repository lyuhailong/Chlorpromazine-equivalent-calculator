
### 1. 安装 Python
首先，确保你的系统上安装了Python。如果没有，请按照以下步骤安装：

1. **下载 Python：**
   - 打开浏览器，访问 [Python 官网](https://www.python.org/).
   - 点击“Downloads”菜单，然后选择适合你操作系统的Python版本（推荐使用最新的Python 3.x版本）。

2. **安装 Python：**
   - 下载完成后，运行安装程序。
   - 在安装向导中，确保勾选“Add Python to PATH”选项，这样可以在命令行中直接使用`python`命令。
   - 点击“Install Now”进行安装。

3. **验证安装：**
   - 打开命令行窗口（按 `Win + R`，输入 `cmd`，然后按回车键）。
   - 输入 `python --version` 以验证Python是否正确安装。应该看到类似于 `Python 3.x.x` 的输出。

### 2. 安装 pip
`pip` 是Python的包管理工具，通常在安装Python时会自动安装。如果没有安装，可以手动安装：

1. **验证 pip：**
   - 在命令行中输入 `pip --version` 以查看pip是否已安装。

2. **安装 pip：**
   - 如果没有安装pip，可以按照以下步骤操作：
     - 下载 [get-pip.py](https://bootstrap.pypa.io/get-pip.py) 文件。
     - 打开命令行，导航到下载文件的目录。
     - 运行 `python get-pip.py`。

### 3. 安装 PyInstaller （如果没有安装的话）
安装 `PyInstaller` 以便将Python脚本打包成可执行文件：

1. **安装 PyInstaller：**
   - 在命令行中输入 `pip install pyinstaller`。

2. **验证安装：**
   - 输入 `pyinstaller --version` 以确保PyInstaller已正确安装。

### 4. 安装TKinter (如果没有安装的话)
- 在命令行中输入 `pip install tk`。

### 5. 下载 Python 脚本

此处为cpzs-v*.py

### 6. 运行可执行文件

- 在命令行中导航到脚本所在的目录。

	例如，如果脚本在 `C:\Users\YourUsername\scripts` 目录中，输入：
`
cd C:\Users\YourUsername\scripts`
运行以下命令将脚本使用`PyInstaller`打包成可执行文件：

	`pyinstaller --onefile --windowed copzs-v*.py`
	
	`--windowed` 参数确保生成的程序不会打开命令行窗口。
	
- 在dist目录中找到生成的可执行文件，双击 `chlorpromazine_calculator.exe` 文件，即可运行程序。


