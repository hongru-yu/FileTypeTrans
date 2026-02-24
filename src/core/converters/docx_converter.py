"""
Word文档转换器模块
"""
from pathlib import Path
from typing import Set

from docx import Document


class DocxConverter:
    """Word文档转换器"""

    # 支持的文件扩展名
    SUPPORTED_EXTENSIONS: Set[str] = {".docx", ".doc"}

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
        转换Word文档为Markdown格式

        Args:
            file_path: 文件路径

        Returns:
            Markdown内容
        """
        # 读取Word文档
        doc = Document(file_path)

        # 构建Markdown内容
        markdown = []
        markdown.append(f"# 原始文件: {file_path.name}\n")
        markdown.append("---\n")

        # 提取所有段落文本
        # 使用 text 属性，它会自动包含所有 runs 的内容
        for paragraph in doc.paragraphs:
            paragraph_text = paragraph.text.strip()
            if paragraph_text:  # 只添加非空段落
                markdown.append(paragraph_text)

        return "\n".join(markdown)
