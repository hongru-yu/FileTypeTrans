"""
FileTypeTrans 项目入口脚本
"""
import sys
from pathlib import Path

# 将 src 目录添加到 Python 路径
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

# 导入并运行主函数
from main import main

if __name__ == "__main__":
    main()
