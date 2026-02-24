"""
FileTypeTrans 主入口文件
"""
import sys
from pathlib import Path

# 将项目根目录添加到 Python 路径
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

# 导入并运行主函数
from src.main import main as cli_main
from src.ui.gui.main_window import main as gui_main

if __name__ == "__main__":
    # 检查命令行参数
    if "--gui" in sys.argv:
        try:
            gui_main()
        except ImportError as e:
            print("错误: PyQt5 未安装，无法启动 GUI")
            print("请运行: uv add PyQt5")
            sys.exit(1)
    else:
        cli_main()
