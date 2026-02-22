"""
目录遍历模块
"""
from pathlib import Path
from typing import Generator, Set

from src.config.config import Config


class DirectoryTraversal:
    """目录遍历类"""

    def __init__(self, source_dir: Path, config: Config):
        """
        初始化目录遍历器

        Args:
            source_dir: 源目录路径
            config: 配置对象
        """
        self.source_dir = source_dir
        self.config = config
        self.total_files = 0
        self.supported_files = 0
        self.skipped_files = 0
        self._visited_files: Set[Path] = set()

    def collect_files(self) -> Generator[Path, None, None]:
        """
        收集所有需要处理的文件

        Yields:
            文件路径
        """
        self.total_files = 0
        self.supported_files = 0
        self.skipped_files = 0
        self._visited_files.clear()

        yield from self._traverse_directory(self.source_dir)

    def _traverse_directory(self, directory: Path) -> Generator[Path, None, None]:
        """
        递归遍历目录

        Args:
            directory: 当前目录路径

        Yields:
            文件路径
        """
        for item in directory.iterdir():
            if item.is_file():
                self.total_files += 1
                item_ext = self.get_file_extension(item.name)

                if self.config.is_supported_extension(item_ext):
                    self.supported_files += 1
                    self._visited_files.add(item)
                    yield item
                else:
                    self.skipped_files += 1

            elif item.is_dir():
                if self.config.should_process_directory(item.name):
                    yield from self._traverse_directory(item)

    @staticmethod
    def get_file_extension(file_name: str) -> str:
        """
        获取文件扩展名

        Args:
            file_name: 文件名

        Returns:
            文件扩展名（包含点号）
        """
        return Path(file_name).suffix
