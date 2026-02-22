"""
命令行界面模块的单元测试
"""
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from src.ui.cli import CLI


class TestCLI:
    """测试命令行界面类"""

    def test_initialization(self):
        """测试初始化"""
        cli = CLI()

        assert cli.source_dir is None
        assert cli.target_dir is None

    def test_set_source_dir(self, tmp_path):
        """测试设置源目录"""
        cli = CLI()
        cli.set_source_dir(tmp_path)

        assert cli.source_dir == tmp_path

    def test_set_target_dir(self, tmp_path):
        """测试设置目标目录"""
        cli = CLI()
        cli.set_target_dir(tmp_path)

        assert cli.target_dir == tmp_path

    def test_validate_source_dir_not_set(self, tmp_path):
        """测试验证未设置源目录"""
        cli = CLI()

        with pytest.raises(ValueError, match="源目录未设置"):
            cli.validate()

    # 注释掉交互式测试，避免阻塞
    # @patch("builtins.input")
    # def test_prompt_source_dir(self, mock_input):
    #     """测试提示输入源目录"""
    #     pass

    # @patch("builtins.input")
    # @patch("builtins.print")
    # def test_prompt_source_dir_with_validation(self, mock_print, mock_input, tmp_path):
    #     """测试提示输入源目录并进行验证进行验证"""
    #     pass

    @patch("builtins.print")
    def test_display_welcome(self, mock_print):
        """测试显示欢迎信息"""
        cli = CLI()
        cli.display_welcome()

        assert mock_print.called
        call_args = [str(call) for call in mock_print.call_args_list]
        assert any("FileTypeTrans" in args for args in call_args)

    @patch("builtins.print")
    def test_display_progress(self, mock_print):
        """测试显示进度"""
        cli = CLI()
        cli.display_progress("test.txt", 5, 10)

        assert mock_print.called

    @patch("builtins.print")
    def test_display_summary(self, mock_print):
        """测试显示摘要"""
        cli = CLI()
        summary = {
            "total": 10,
            "success": 5,
            "failed": 2,
            "skipped": 3,
        }
        cli.display_summary(summary)

        assert mock_print.called
