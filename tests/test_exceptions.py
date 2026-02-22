"""
异常处理模块的单元测试
"""
import pytest
from src.utils.exceptions import (
    ConversionError,
    FileNotFoundError,
    UnsupportedFormatError,
)


class TestConversionError:
    """测试转换错误"""

    def test_initialization(self):
        """测试初始化"""
        error = ConversionError("转换失败")
        assert str(error) == "转换失败"

    def test_with_file_path(self):
        """测试带文件路径的转换错误"""
        error = ConversionError("转换失败", file_path="/test/file.txt")
        assert "转换失败" in str(error)


class TestFileNotFoundError:
    """测试文件未找到错误"""

    def test_initialization(self):
        """测试初始化"""
        error = FileNotFoundError("文件未找到")
        assert str(error) == "文件未找到"

    def test_is_conversion_error(self):
        """测试是否是转换错误"""
        error = FileNotFoundError("文件未找到")
        assert isinstance(error, ConversionError)


class TestUnsupportedFormatError:
    """测试不支持格式错误"""

    def test_initialization(self):
        """测试初始化"""
        error = UnsupportedFormatError("不支持的格式")
        assert str(error) == "不支持的格式"

    def test_with_file_format(self):
        """测试带文件格式的不支持错误"""
        error = UnsupportedFormatError("不支持的格式", file_format=".xyz")
        assert "不支持的格式" in str(error)
        assert ".xyz" in str(error)

    def test_is_conversion_error(self):
        """测试是否是转换错误"""
        error = UnsupportedFormatError("不支持的格式")
        assert isinstance(error, ConversionError)
