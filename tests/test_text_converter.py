"""
文本转换器模块的单元测试
"""
import pytest
from pathlib import Path
from src.core.converters.text_converter import TextConverter


class TestTextConverter:
    """测试文本转换器类"""

    def test_convert_txt_to_markdown(self, tmp_path):
        """测试转换 .txt 文件"""
        # 创建测试文件
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, World!\n\nThis is a test file.")

        converter = TextConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: test.txt" in markdown
        assert "Hello, World!" in markdown
        assert "This is a test file." in markdown

    def test_convert_md_to_markdown(self, tmp_path):
        """测试转换 .md 文件（已经是 Markdown）"""
        test_file = tmp_path / "test.md"
        test_file.write_text("# Title\n\nContent here.")

        converter = TextConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: test.md" in markdown
        assert "# Title" in markdown
        assert "Content here." in markdown

    def test_convert_rst_to_markdown(self, tmp_path):
        """测试转换 .rst 文件"""
        test_file = tmp_path / "test.rst"
        test_file.write_text("Title\n=====\n\nSome content.")

        converter = TextConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: test.rst" in markdown
        assert "Title" in markdown
        assert "Some content." in markdown

    def test_convert_empty_file(self, tmp_path):
        """测试转换空文件"""
        test_file = tmp_path / "empty.txt"
        test_file.write_text("")

        converter = TextConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: empty.txt" in markdown

    def test_convert_large_file(self, tmp_path):
        """测试转换大文件"""
        test_file = tmp_path / "large.txt"
        content = "Line {}\n".format("test") * 1000
        test_file.write_text(content)

        converter = TextConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: large.txt" in markdown
        assert "Line test" in markdown

    def test_convert_file_with_special_characters(self, tmp_path):
        """测试转换包含特殊字符的文件"""
        test_file = tmp_path / "special.txt"
        test_file.write_text("Hello: 你好\nNumbers: 123\nSymbols: @#$%")

        converter = TextConverter()
        markdown = converter.convert(test_file)

        assert "Hello: 你好" in markdown
        assert "Numbers: 123" in markdown
        assert "Symbols: @#$%" in markdown

    def test_supports_txt(self):
        """测试是否支持 .txt 文件"""
        converter = TextConverter()
        assert converter.supports(".txt")

    def test_supports_md(self):
        """测试是否支持 .md 文件"""
        converter = TextConverter()
        assert converter.supports(".md")

    def test_supports_rst(self):
        """测试是否支持 .rst 文件"""
        converter = TextConverter()
        assert converter.supports(".rst")

    def test_supports_adoc(self):
        """测试是否支持 .adoc 文件"""
        converter = TextConverter()
        assert converter.supports(".adoc")

    def test_does_not_support_other_formats(self):
        """测试不支持其他格式"""
        converter = TextConverter()
        assert not converter.supports(".pdf")
        assert not converter.supports(".docx")
        assert not converter.supports(".xlsx")
