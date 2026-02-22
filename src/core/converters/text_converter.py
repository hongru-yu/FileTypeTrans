"""
文本文件转换器模块
"""
from pathlib import Path
from typing import Set

from core.file_handler import FileHandler
from config.constants import SUPPORTED_TEXT_EXTENSIONS


class TextConverter:
    """文本文件转换器"""

    SUPPORTED_EXTENSIONS = SUPPORTED_TEXT_EXTENSIONS

    def __init__(self):
        self.file_handler = FileHandler()

    def supports(self, file_extension: str) -> bool:
        """
        判断是否支持该文件类型

        Args:
            file_extension: 文件扩展名

        Returns:
            是否支持
        """
        return file_extension.lower() in SUPPORTED_TEXT_EXTENSIONS

    def convert(self, file_path: Path) -> str:
        """
        转换文件为 Markdown 格式

        Args:
            file_path: 文件路径

        Returns:
            Markdown 内容
        """
        # 读取文件内容
        content = self.file_handler.read_file_content(file_path)

        # 构建 Markdown 内容
        markdown = []
        markdown.append(f"# 原始文件: {file_path.name}\n")
        markdown.append("---\n")
        markdown.append(content)

        return "\n".join(markdown)
