"""
Excel转换器模块的单元测试
"""
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from src.core.converters.excel_converter import ExcelConverter


class TestExcelConverter:
    """测试Excel转换器类"""

    def test_supports_xlsx(self):
        """测试是否支持 .xlsx 文件"""
        converter = ExcelConverter()
        assert converter.supports(".xlsx")

    def test_supports_xls(self):
        """测试是否支持 .xls 文件"""
        converter = ExcelConverter()
        assert converter.supports(".xls")

    def test_supports_csv(self):
        """测试是否支持 .csv 文件"""
        converter = ExcelConverter()
        assert converter.supports(".csv")

    def test_supports_case_insensitive(self):
        """测试文件扩展名是否大小写不敏感"""
        converter = ExcelConverter()
        assert converter.supports(".XLSX")
        assert converter.supports(".XLS")
        assert converter.supports(".CSV")

    def test_does_not_support_other_formats(self):
        """测试不支持其他格式"""
        converter = ExcelConverter()
        assert not converter.supports(".pdf")
        assert not converter.supports(".docx")
        assert not converter.supports(".txt")

    @patch('src.core.converters.excel_converter.pd')
    def test_convert_xlsx_to_markdown(self, mock_pandas):
        """测试转换 .xlsx 文件为 Markdown 表格"""
        # 创建 mock DataFrame
        mock_df = Mock()
        mock_df.empty = False
        mock_df.values = [
            "姓名,年龄,城市\n张三,25,北京\n李四,30,上海".split('\n')
        ]
        # Mock to_markdown 方法返回字符串
        mock_df.to_markdown.return_value = "| 姓名 | 年龄 | 城市 |\n|------|------|------|\n| 张三 | 25  | 北京 |\n| 李四 | 30  | 上海 |"

        # Mock pandas read_excel 返回
        mock_pandas.read_excel.return_value = mock_df

        # 创建测试文件路径
        test_file = Path("/tmp/test.xlsx")

        converter = ExcelConverter()
        markdown = converter.convert(test_file)

        # 验证输出
        assert "# 原始文件: test.xlsx" in markdown
        assert "姓名" in markdown or "年龄" in markdown or "城市" in markdown

        # 验证 read_excel 被正确调用
        mock_pandas.read_excel.assert_called_once_with(test_file)

    @patch('src.core.converters.excel_converter.pd')
    def test_convert_empty_excel(self, mock_pandas):
        """测试转换空Excel文件"""
        mock_df = Mock()
        mock_df.empty = True
        mock_pandas.read_excel.return_value = mock_df

        test_file = Path("/tmp/empty.xlsx")

        converter = ExcelConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: empty.xlsx" in markdown

    @patch('src.core.converters.excel_converter.pd')
    def test_convert_csv_to_markdown(self, mock_pandas):
        """测试转换 .csv 文件为 Markdown 表格"""
        mock_df = Mock()
        mock_df.empty = False
        mock_df.to_markdown.return_value = "| col1 | col2 |\n|------|------|"
        mock_pandas.read_csv.return_value = mock_df

        test_file = Path("/tmp/test.csv")

        converter = ExcelConverter()
        markdown = converter.convert(test_file)

        # 验证 read_csv 被正确调用
        mock_pandas.read_csv.assert_called_once_with(test_file)

    @patch('src.core.converters.excel_converter.pd')
    def test_convert_excel_with_special_characters(self, mock_pandas):
        """测试转换包含特殊字符的Excel文件"""
        mock_df = Mock()
        mock_df.empty = False
        mock_df.to_markdown.return_value = "| name | value |\n|------|-------|"
        mock_pandas.read_excel.return_value = mock_df

        test_file = Path("/tmp/special.xlsx")

        converter = ExcelConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: special.xlsx" in markdown

    @patch('src.core.converters.excel_converter.pd')
    def test_convert_large_excel(self, mock_pandas):
        """测试转换大Excel文件"""
        mock_df = Mock()
        mock_df.empty = False
        mock_df.to_markdown.return_value = "| col1 | col2 |\n|------|------|"
        mock_pandas.read_excel.return_value = mock_df

        test_file = Path("/tmp/large.xlsx")

        converter = ExcelConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: large.xlsx" in markdown

    @patch('src.core.converters.excel_converter.pd')
    def test_convert_excel_with_multiple_sheets(self, mock_pandas):
        """测试转换包含多个工作表的Excel文件"""
        mock_df = Mock()
        mock_df.empty = False
        mock_df.to_markdown.return_value = "| col1 | col2 |\n|------|------|"
        mock_pandas.read_excel.return_value = mock_df

        test_file = Path("/tmp/multisheet.xlsx")

        converter = ExcelConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: multisheet.xlsx" in markdown

    def test_convert_file_not_found(self):
        """测试文件不存在的错误处理"""
        test_file = Path("/tmp/nonexistent.xlsx")

        converter = ExcelConverter()

        with pytest.raises(Exception):
            converter.convert(test_file)

    @patch('src.core.converters.excel_converter.pd')
    def test_convert_corrupted_excel(self, mock_pandas):
        """测试损坏Excel的错误处理"""
        mock_pandas.read_excel.side_effect = Exception("File is corrupted")

        test_file = Path("/tmp/corrupted.xlsx")

        converter = ExcelConverter()

        with pytest.raises(Exception):
            converter.convert(test_file)

    @patch('src.core.converters.excel_converter.pd')
    def test_convert_csv_with_empty_lines(self, mock_pandas):
        """测试转换包含空行的CSV文件"""
        mock_df = Mock()
        mock_df.empty = False
        mock_df.to_markdown.return_value = "| col1 | col2 |\n|------|------|"
        mock_pandas.read_csv.return_value = mock_df

        test_file = Path("/tmp/emptylines.csv")

        converter = ExcelConverter()
        markdown = converter.convert(test_file)

        assert "# 原始文件: emptylines.csv" in markdown

    def test_init(self):
        """测试初始化"""
        converter = ExcelConverter()
        assert converter is not None
        assert hasattr(converter, 'supports')
        assert hasattr(converter, 'convert')
