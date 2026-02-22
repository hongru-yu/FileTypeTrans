"""
Excel文档转换器模块
"""
from pathlib import Path
from typing import Set
import pandas as pd


class ExcelConverter:
    """Excel文档转换器"""

    # 支持的文件扩展名
    SUPPORTED_EXTENSIONS: Set[str] = {".xlsx", ".xls", ".csv"}

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
        转换Excel文档为Markdown表格格式

        Args:
            file_path: 文件路径

        Returns:
            Markdown内容
        """
        # 读取Excel/CSV文档
        file_extension = file_path.suffix.lower()

        if file_extension == ".csv":
            df = pd.read_csv(file_path)
        else:
            # xlsx 或 xls
            df = pd.read_excel(file_path)

        # 构建Markdown内容
        markdown = []
        markdown.append(f"# 原始文件: {file_path.name}\n")
        markdown.append("---\n")

        # 如果DataFrame为空，只返回标题
        if df.empty:
            return "\n".join(markdown)

        # 转换为Markdown表格
        markdown.append(df.to_markdown(index=False))

        return "\n".join(markdown)
