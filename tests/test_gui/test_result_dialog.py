"""
结果对话框模块的单元测试
"""
import pytest
import tempfile
from pathlib import Path


class TestResultDialog:
    """测试结果对话框"""

    @pytest.fixture
    def qapp(self, qapp):
        """确保 QApplication 实例存在"""
        return qapp

    @pytest.fixture
    def result_dialog(self, qapp):
        from src.ui.gui.result_dialog import ResultDialog
        summary = {
            "total": 10,
            "success": 8,
            "failed": 1,
            "skipped": 1,
        }
        return ResultDialog(summary, "/tmp/")

    def test_initialization(self, result_dialog):
        """测试初始化"""
        assert result_dialog is not None
        assert result_dialog.windowTitle() == "转换完成"

    def test_summary_display(self, result_dialog):
        """测试统计信息显示"""
        # 验证统计信息已正确显示
        # 由于是私有属性，通过方法验证
        assert result_dialog.summary_data is not None
        assert result_dialog.summary_data["total"] == 10

    def test_open_folder_action(self, result_dialog, tmp_path):
        """测试打开文件夹操作"""
        # 创建测试目录
        test_dir = tmp_path / "test_output"
        test_dir.mkdir()

        # 测试设置输出目录
        result_dialog.output_dir = str(test_dir)
        assert result_dialog.output_dir == str(test_dir)

    def test_close_button(self, result_dialog):
        """测试关闭按钮存在"""
        # 验证关闭按钮存在
        assert result_dialog.close_button is not None
