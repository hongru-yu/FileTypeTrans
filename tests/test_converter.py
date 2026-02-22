"""
转换器基类和选择逻辑的单元测试
"""
import pytest
from pathlib import Path
from src.core.converter import ConverterRegistry, get_converter
from src.core.converters.text_converter import TextConverter
from src.core.converters.docx_converter import DocxConverter
from src.core.converters.pdf_converter import PdfConverter
from src.core.converters.excel_converter import ExcelConverter
from src.core.converters.pptx_converter import PptxConverter


class TestConverterRegistry:
    """测试转换器注册表"""

    def test_register_converter(self, tmp_path):
        """测试注册转换器"""
        registry = ConverterRegistry()
        converter = TextConverter()

        registry.register(converter)

        assert ".txt" in registry._converters
        assert ".md" in registry._converters
        assert ".rst" in registry._converters

    def test_register_multiple_converters(self, tmp_path):
        """测试注册多个转换器"""
        registry = ConverterRegistry()

        registry.register(TextConverter())
        registry.register(DocxConverter())
        registry.register(PdfConverter())
        registry.register(ExcelConverter())
        registry.register(PptxConverter())

        # 检查支持的扩展名数量
        assert len(registry._converters) > 0

    def test_get_converter_for_txt(self, tmp_path):
        """测试获取 TXT 转换器"""
        registry = ConverterRegistry()
        registry.register(TextConverter())

        converter = registry.get_converter(".txt")
        assert converter is not None
        assert isinstance(converter, TextConverter)

    def test_get_converter_for_docx(self, tmp_path):
        """测试获取 DOCX 转换器"""
        registry = ConverterRegistry()
        registry.register(DocxConverter())

        converter = registry.get_converter(".docx")
        assert converter is not None
        assert isinstance(converter, DocxConverter)

    def test_get_converter_for_pdf(self, tmp_path):
        """测试获取 PDF 转换器"""
        registry = ConverterRegistry()
        registry.register(PdfConverter())

        converter = registry.get_converter(".pdf")
        assert converter is not None
        assert isinstance(converter, PdfConverter)

    def test_get_converter_for_unsupported_format(self, tmp_path):
        """测试获取不支持格式的转换器"""
        registry = ConverterRegistry()
        registry.register(TextConverter())

        converter = registry.get_converter(".unsupported")
        assert converter is None

    def test_case_insensitive_extension(self, tmp_path):
        """测试扩展名大小写不敏感"""
        registry = ConverterRegistry()
        registry.register(TextConverter())

        converter1 = registry.get_converter(".TXT")
        converter2 = registry.get_converter(".txt")
        converter3 = registry.get_converter(".TxT")

        assert converter1 is not None
        assert converter2 is not None
        assert converter3 is not None
        assert isinstance(converter1, TextConverter)
        assert isinstance(converter2, TextConverter)
        assert isinstance(converter3, TextConverter)


class TestGetConverter:
    """测试获取转换器的全局函数"""

    def test_get_converter_for_txt(self):
        """测试获取 TXT 转换器"""
        converter = get_converter(Path("test.txt"))
        assert converter is not None
        assert isinstance(converter, TextConverter)

    def test_get_converter_for_docx(self):
        """测试获取 DOCX 转换器"""
        converter = get_converter(Path("test.docx"))
        assert converter is not None
        assert isinstance(converter, DocxConverter)

    def test_get_converter_for_doc(self):
        """测试获取 DOC 转换器"""
        converter = get_converter(Path("test.doc"))
        assert converter is not None
        assert isinstance(converter, DocxConverter)

    def test_get_converter_for_pdf(self):
        """测试获取 PDF 转换器"""
        converter = get_converter(Path("test.pdf"))
        assert converter is not None
        assert isinstance(converter, PdfConverter)

    def test_get_converter_for_xlsx(self):
        """测试获取 XLSX 转换器"""
        converter = get_converter(Path("test.xlsx"))
        assert converter is not None
        assert isinstance(converter, ExcelConverter)

    def test_get_converter_for_xls(self):
        """测试获取 XLS 转换器"""
        converter = get_converter(Path("test.xls"))
        assert converter is not None
        assert isinstance(converter, ExcelConverter)

    def test_get_converter_for_csv(self):
        """测试获取 CSV 转换器"""
        converter = get_converter(Path("test.csv"))
        assert converter is not None
        assert isinstance(converter, ExcelConverter)

    def test_get_converter_for_pptx(self):
        """测试获取 PPTX 转换器"""
        converter = get_converter(Path("test.pptx"))
        assert converter is not None
        assert isinstance(converter, PptxConverter)

    def test_get_converter_for_ppt(self):
        """测试获取 PPT 转换器"""
        converter = get_converter(Path("test.ppt"))
        assert converter is not None
        assert isinstance(converter, PptxConverter)

    def test_get_converter_for_unsupported_format(self):
        """测试获取不支持格式的转换器"""
        converter = get_converter(Path("test.unsupported"))
        assert converter is None

    def test_get_converter_for_image(self):
        """测试获取图片格式转换器"""
        converter = get_converter(Path("test.png"))
        assert converter is None

    def test_get_converter_for_code(self):
        """测试获取代码格式转换器"""
        converter = get_converter(Path("test.py"))
        assert converter is None
