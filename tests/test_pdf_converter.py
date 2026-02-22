"""
PDF转换器模块的单元测试
"""
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from src.core.converters.pdf_converter import PdfConverter


class TestPdfConverter:
    """测试PDF转换器类"""

    def test_supports_pdf(self):
        """测试是否支持 .pdf 文件"""
        converter = PdfConverter()
        assert converter.supports(".pdf")

    def test_supports_case_insensitive(self):
        """测试文件扩展名是否大小写不敏感"""
        converter = PdfConverter()
        assert converter.supports(".PDF")
        assert converter.supports(".Pdf")

    def test_does_not_support_other_formats(self):
        """测试不支持其他格式"""
        converter = PdfConverter()
        assert not converter.supports(".docx")
        assert not converter.supports(".xlsx")
        assert not converter.supports(".txt")

    @patch('src.core.converters.pdf_converter.PdfReader')
    def test_convert_pdf_to_markdown(self, mock_pdf_reader_class):
        """测试转换 .pdf 文件为 Markdown"""
        # 创建 mock PDF reader
        mock_reader = Mock()
        mock_pdf_reader_class.return_value = mock_reader

        # 创建 mock 页面
        mock_page1 = Mock()
        mock_page1.extract_text.return_value = "这是第一页的内容。\n包含多行文本。"
        mock_page2 = Mock()
        mock_page2.extract_text.return_value = "这是第二页的内容。\n更多文本。"

        mock_reader.pages = [mock_page1, mock_page2]

        # 创建测试文件路径
        test_file = Path("/tmp/test.pdf")

        converter = PdfConverter()
        markdown = converter.convert(test_file)

        # 验证输出
        assert "# 原始文件: test.pdf" in markdown
        assert "这是第一页的内容。" in markdown
        assert "包含多行文本。" in markdown
        assert "这是第二页的内容。" in markdown
        assert "更多文本。" in markdown

        # 验证 PdfReader 被正确调用
        mock_pdf_reader_class.assert_called_once_with(test_file)

    @patch('src.core.converters.pdf_converter.PdfReader')
    def test_convert_empty_pdf(self, mock_pdf_reader_class):
        """测试转换空PDF"""
        mock_reader = Mock()
        mock_pdf_reader_class.return_value = mock_reader
        mock_reader.pages = []

        test_file = Path("/tmp/empty.pdf")

        converter = PdfConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: empty.pdf" in markdown

    @patch('src.core.converters.pdf_converter.PdfReader')
    def test_convert_pdf_with_empty_pages(self, mock_pdf_reader_class):
        """测试转换包含空页面的PDF"""
        mock_reader = Mock()
        mock_pdf_reader_class.return_value = mock_reader

        mock_page1 = Mock()
        mock_page1.extract_text.return_value = "第一页内容"
        mock_page2 = Mock()
        mock_page2.extract_text.return_value = ""
        mock_page3 = Mock()
        mock_page3.extract_text.return_value = "第三页内容"

        mock_reader.pages = [mock_page1, mock_page2, mock_page3]

        test_file = Path("/tmp/mixed.pdf")

        converter = PdfConverter()
        markdown = converter.convert(test_file)

        assert "第一页内容" in markdown
        assert "第三页内容" in markdown

    @patch('src.core.converters.pdf_converter.PdfReader')
    def test_convert_pdf_with_special_characters(self, mock_pdf_reader_class):
        """测试转换包含特殊字符的PDF"""
        mock_reader = Mock()
        mock_pdf_reader_class.return_value = mock_reader

        mock_page = Mock()
        mock_page.extract_text.return_value = "中文：你好\n数字：123\n符号：@#$%"
        mock_reader.pages = [mock_page]

        test_file = Path("/tmp/special.pdf")

        converter = PdfConverter()
        markdown = converter.convert(test_file)

        assert "中文：你好" in markdown
        assert "数字：123" in markdown
        assert "符号：@#$%" in markdown

    @patch('src.core.converters.pdf_converter.PdfReader')
    def test_convert_large_pdf(self, mock_pdf_reader_class):
        """测试转换大PDF"""
        mock_reader = Mock()
        mock_pdf_reader_class.return_value = mock_reader

        # 创建10个页面
        pages = []
        for i in range(10):
            mock_page = Mock()
            mock_page.extract_text.return_value = f"这是第 {i+1} 页的内容"
            pages.append(mock_page)

        mock_reader.pages = pages

        test_file = Path("/tmp/large.pdf")

        converter = PdfConverter()
        markdown = converter.convert(test_file)

        assert "这是第 1 页的内容" in markdown
        assert "这是第 10 页的内容" in markdown

    def test_convert_file_not_found(self):
        """测试文件不存在的错误处理"""
        test_file = Path("/tmp/nonexistent.pdf")

        converter = PdfConverter()

        with pytest.raises(Exception):
            converter.convert(test_file)

    @patch('src.core.converters.pdf_converter.PdfReader')
    def test_convert_corrupted_pdf(self, mock_pdf_reader_class):
        """测试损坏PDF的错误处理"""
        from PyPDF2.errors import PdfReadError

        mock_pdf_reader_class.side_effect = PdfReadError("PDF is corrupted")

        test_file = Path("/tmp/corrupted.pdf")

        converter = PdfConverter()

        with pytest.raises(PdfReadError):
            converter.convert(test_file)

    @patch('src.core.converters.pdf_converter.PdfReader')
    def test_convert_pdf_with_multiline_text_per_page(self, mock_pdf_reader_class):
        """测试转换每页包含多行文本的PDF"""
        mock_reader = Mock()
        mock_pdf_reader_class.return_value = mock_reader

        mock_page = Mock()
        mock_page.extract_text.return_value = "标题\n\n副标题\n\n内容第一行\n内容第二行\n内容第三行"
        mock_reader.pages = [mock_page]

        test_file = Path("/tmp/multiline.pdf")

        converter = PdfConverter()
        markdown = converter.convert(test_file)

        assert "标题" in markdown
        assert "副标题" in markdown
        assert "内容第一行" in markdown
        assert "内容第二行" in markdown
        assert "内容第三行" in markdown

    def test_init(self):
        """测试初始化"""
        converter = PdfConverter()
        assert converter is not None
        assert hasattr(converter, 'supports')
        assert hasattr(converter, 'convert')
