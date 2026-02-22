"""
命令行界面模块
"""
from pathlib import Path
from typing import Optional, Dict, Any


class CLI:
    """命令行界面类"""

    def __init__(self):
        """初始化"""
        self.source_dir: Optional[Path] = None
        self.target_dir: Optional[Path] = None

    def set_source_dir(self, path: Path) -> None:
        """
        设置源目录

        Args:
            path: 源目录路径
        """
        self.source_dir = path

    def set_target_dir(self, path: Path) -> None:
        """
        设置目标目录

        Args:
            path: 目标目录路径
        """
        self.target_dir = path

    def validate(self) -> bool:
        """
        验证设置

        Returns:
            验证是否通过

        Raises:
            ValueError: 验证失败
        """
        if self.source_dir is None:
            raise ValueError("源目录未设置")

        if not self.source_dir.exists():
            raise ValueError(f"源目录不存在: {self.source_dir}")

        if not self.source_dir.is_dir():
            raise ValueError(f"源路径不是目录: {self.source_dir}")

        return True

    def prompt_source_dir(self) -> None:
        """提示用户输入源目录"""
        import builtins

        while True:
            path_str = builtins.input("请输入源目录路径: ")
            path = Path(path_str)

            if path.exists() and path.is_dir():
                self.source_dir = path
                break
            else:
                builtins.print(f"错误: 目录不存在或无效: {path_str}")

    def display_welcome(self) -> None:
        """显示欢迎信息"""
        import builtins

        builtins.print("=" * 50)
        builtins.print("欢迎使用 FileTypeTrans 文件格式转换工具")
        builtins.print("=" * 50)
        builtins.print()

    def display_progress(self, file_name: str, current: int, total: int) -> None:
        """
        显示转换进度

        Args:
            file_name: 当前处理文件名
            current: 当前已处理数量
            total: 总文件数量
        """
        import builtins

        percentage = (current / total * 100) if total > 0 else 0
        builtins.print(f"\r处理中: {file_name} [{current}/{total}] ({percentage:.1f}%)", end="", flush=True)

    def display_summary(self, summary: Dict[str, Any]) -> None:
        """
        显示转换摘要

        Args:
            summary: 摘要信息字典
        """
        import builtins

        builtins.print()
        builtins.print("=" * 50)
        builtins.print("转换完成!")
        builtins.print("=" * 50)
        builtins.print(f"总文件数: {summary.get('total', 0)}")
        builtins.print(f"成功: {summary.get('success', 0)}")
        builtins.print(f"失败: {summary.get('failed', 0)}")
        builtins.print(f"跳过: {summary.get('skipped', 0)}")
        builtins.print("=" * 50)
