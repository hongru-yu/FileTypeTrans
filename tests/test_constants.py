"""
配置常量模块的单元测试
"""
import pytest

from src.config.constants import (
    SUPPORTED_TEXT_EXTENSIONS,
    SUPPORTED_DOCX_EXTENSIONS,
    SUPPORTED_PDF_EXTENSIONS,
    SUPPORTED_EXCEL_EXTENSIONS,
    SUPPORTED_PPTX_EXTENSIONS,
    ALL_SUPPORTED_EXTENSIONS,
    EXCLUDED_DIRECTORIES,
    IMAGE_EXTENSIONS,
    CODE_EXTENSIONS,
    CONFIG_EXTENSIONS,
    ARCHIVE_EXTENSIONS,
    EXECUTABLE_EXTENSIONS,
    ALL_SKIPPED_EXTENSIONS,
)


class TestSupportedExtensions:
    """测试支持的文件扩展名"""

    def test_supported_text_extensions(self):
        """测试支持的文本文件扩展名"""
        assert isinstance(SUPPORTED_TEXT_EXTENSIONS, set)
        assert ".txt" in SUPPORTED_TEXT_EXTENSIONS
        assert ".md" in SUPPORTED_TEXT_EXTENSIONS
        assert ".rst" in SUPPORTED_TEXT_EXTENSIONS
        assert ".adoc" in SUPPORTED_TEXT_EXTENSIONS

    def test_supported_docx_extensions(self):
        """测试支持的 Word 文档扩展名"""
        assert isinstance(SUPPORTED_DOCX_EXTENSIONS, set)
        assert ".docx" in SUPPORTED_DOCX_EXTENSIONS
        assert ".doc" in SUPPORTED_DOCX_EXTENSIONS

    def test_supported_pdf_extensions(self):
        """测试支持的 PDF 扩展名"""
        assert isinstance(SUPPORTED_PDF_EXTENSIONS, set)
        assert ".pdf" in SUPPORTED_PDF_EXTENSIONS

    def test_supported_excel_extensions(self):
        """测试支持的 Excel 扩展名"""
        assert isinstance(SUPPORTED_EXCEL_EXTENSIONS, set)
        assert ".xlsx" in SUPPORTED_EXCEL_EXTENSIONS
        assert ".xls" in SUPPORTED_EXCEL_EXTENSIONS
        assert ".csv" in SUPPORTED_EXCEL_EXTENSIONS

    def test_supported_pptx_extensions(self):
        """测试支持的 PPT 扩展名"""
        assert isinstance(SUPPORTED_PPTX_EXTENSIONS, set)
        assert ".pptx" in SUPPORTED_PPTX_EXTENSIONS
        assert ".ppt" in SUPPORTED_PPTX_EXTENSIONS

    def test_all_supported_extensions(self):
        """测试所有支持的扩展名集合"""
        assert isinstance(ALL_SUPPORTED_EXTENSIONS, set)
        # 应该包含所有支持的扩展名
        for ext in SUPPORTED_TEXT_EXTENSIONS:
            assert ext in ALL_SUPPORTED_EXTENSIONS
        for ext in SUPPORTED_DOCX_EXTENSIONS:
            assert ext in ALL_SUPPORTED_EXTENSIONS
        for ext in SUPPORTED_PDF_EXTENSIONS:
            assert ext in ALL_SUPPORTED_EXTENSIONS
        for ext in SUPPORTED_EXCEL_EXTENSIONS:
            assert ext in ALL_SUPPORTED_EXTENSIONS
        for ext in SUPPORTED_PPTX_EXTENSIONS:
            assert ext in ALL_SUPPORTED_EXTENSIONS


class TestExcludedDirectories:
    """测试排除的目录"""

    def test_excluded_directories(self):
        """测试排除的目录列表"""
        assert isinstance(EXCLUDED_DIRECTORIES, set)
        assert ".git" in EXCLUDED_DIRECTORIES
        assert "__pycache__" in EXCLUDED_DIRECTORIES
        assert "node_modules" in EXCLUDED_DIRECTORIES
        assert ".venv" in EXCLUDED_DIRECTORIES


class TestSkippedExtensions:
    """测试跳过的文件扩展名"""

    def test_image_extensions(self):
        """测试图片扩展名"""
        assert isinstance(IMAGE_EXTENSIONS, set)
        assert ".png" in IMAGE_EXTENSIONS
        assert ".jpg" in IMAGE_EXTENSIONS
        assert ".jpeg" in IMAGE_EXTENSIONS
        assert ".gif" in IMAGE_EXTENSIONS
        assert ".svg" in IMAGE_EXTENSIONS

    def test_code_extensions(self):
        """测试代码文件扩展名"""
        assert isinstance(CODE_EXTENSIONS, set)
        assert ".py" in CODE_EXTENSIONS
        assert ".js" in CODE_EXTENSIONS
        assert ".java" in CODE_EXTENSIONS
        assert ".html" in CODE_EXTENSIONS
        assert ".css" in CODE_EXTENSIONS
        assert ".yaml" in CODE_EXTENSIONS
        assert ".xml" in CODE_EXTENSIONS
        assert ".json" in CODE_EXTENSIONS

    def test_config_extensions(self):
        """测试配置文件扩展名"""
        assert isinstance(CONFIG_EXTENSIONS, set)
        assert ".yml" in CONFIG_EXTENSIONS

    def test_archive_extensions(self):
        """测试压缩文件扩展名"""
        assert isinstance(ARCHIVE_EXTENSIONS, set)
        assert ".zip" in ARCHIVE_EXTENSIONS
        assert ".tar" in ARCHIVE_EXTENSIONS
        assert ".gz" in ARCHIVE_EXTENSIONS

    def test_executable_extensions(self):
        """测试可执行文件扩展名"""
        assert isinstance(EXECUTABLE_EXTENSIONS, set)
        assert ".exe" in EXECUTABLE_EXTENSIONS
        assert ".dmg" in EXECUTABLE_EXTENSIONS
        assert ".app" in EXECUTABLE_EXTENSIONS

    def test_all_skipped_extensions(self):
        """测试所有跳过的扩展名集合"""
        assert isinstance(ALL_SKIPPED_EXTENSIONS, set)
        # 应该包含所有跳过的扩展名
        for ext in IMAGE_EXTENSIONS:
            assert ext in ALL_SKIPPED_EXTENSIONS
        for ext in CODE_EXTENSIONS:
            assert ext in ALL_SKIPPED_EXTENSIONS
        for ext in CONFIG_EXTENSIONS:
            assert ext in ALL_SKIPPED_EXTENSIONS
        for ext in ARCHIVE_EXTENSIONS:
            assert ext in ALL_SKIPPED_EXTENSIONS
        for ext in EXECUTABLE_EXTENSIONS:
            assert ext in ALL_SKIPPED_EXTENSIONS

    def test_no_overlap_between_supported_and_skipped(self):
        """测试支持的扩展名和跳过的扩展名没有重叠"""
        overlap = ALL_SUPPORTED_EXTENSIONS & ALL_SKIPPED_EXTENSIONS
        assert len(overlap) == 0, f"重叠的扩展名: {overlap}"
