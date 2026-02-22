"""
PDF文档转换器模块
"""
from pathlib import Path
from typing import Set

from PyPDF2 import PdfReader


class PdfConverter:
    """PDF文档转换器"""

    # 支持的文件扩展名
    SUPPORTED_EXTENSIONS: Set[str] = {".pdf"}

    def __init__(self):
        """初始化转换器"""
        pass

    def supports(self, file_extension: str) -> bool:
        """
        判断是否支持该文件类型

        Args:
            file_extension: 文件扩展名

        Returns:
            是否支持
        """
        return file_extension.lower() in self.SUPPORTED_EXTENSIONS

    def convert(self, file_path: Path) -> str:
        """
        转换PDF文档为Markdown格式

        Args:
            file_path: 文件路径

        Returns:
            Markdown内容
        """
        # 读取PDF文档
        reader = PdfReader(file_path)

        # 构建Markdown内容
        markdown = []
        markdown.append(f"# 原始文件: {file_path.name}\n")
        markdown.append("---\n")

        # 提取所有页面文本
        for page in reader.pages:
            text = page.extract_text()
            if text:  # 只添加非空文本
                markdown.append(text.strip())

        return "\n".join(markdown)
