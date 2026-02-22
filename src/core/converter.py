"""
转换器基类和转换器注册表
"""
from pathlib import Path
from typing import Dict, Optional

from core.converters.text_converter import TextConverter
from core.converters.docx_converter import DocxConverter
from core.converters.pdf_converter import PdfConverter
from core.converters.excel_converter import ExcelConverter
from core.converters.pptx_converter import PptxConverter


class ConverterRegistry:
    """转换器注册表"""

    def __init__(self):
        self._converters: Dict[str, object] = {}

    def register(self, converter: object) -> None:
        """
        注册转换器

        Args:
            converter: 转换器实例
        """
        # 获取转换器支持的扩展名
        if hasattr(converter, "SUPPORTED_EXTENSIONS"):
            for ext in converter.SUPPORTED_EXTENSIONS:
                self._converters[ext.lower()] = converter

    def get_converter(self, extension: str) -> Optional[object]:
        """
        获取指定扩展名的转换器

        Args:
            extension: 文件扩展名（包含点号）

        Returns:
            转换器实例，如果没有找到则返回 None
        """
        return self._converters.get(extension.lower())


# 创建全局转换器注册表
_global_registry = ConverterRegistry()
_global_registry.register(TextConverter())
_global_registry.register(DocxConverter())
_global_registry.register(PdfConverter())
_global_registry.register(ExcelConverter())
_global_registry.register(PptxConverter())


def get_converter(file_path: Path) -> Optional[object]:
    """
    获取文件对应的转换器

    Args:
        file_path: 文件路径

    Returns:
        转换器实例，如果没有找到则返回 None
    """
    extension = file_path.suffix
    return _global_registry.get_converter(extension)
