"""
进度对话框模块的单元测试
"""
import pytest
from PyQt5.QtCore import QEvent


class TestProgressDialog:
    """测试进度对话框"""

    @pytest.fixture
    def qapp(self, qapp):
        """确保 QApplication 实例存在"""
        return qapp

    @pytest.fixture
    def progress_dialog(self, qapp):
        from src.ui.gui.progress_dialog import ProgressDialog
        return ProgressDialog()

    def test_initialization(self, progress_dialog):
        """测试初始化"""
        assert progress_dialog is not None
        assert progress_dialog.windowTitle() == "文件转换进度"

    def test_update_progress(self, progress_dialog):
        """测试更新进度"""
        # 模拟文件名更新
        progress_dialog.update_progress(5, 10, "test.txt")

        # 验证文件标签已更新
        file_label = progress_dialog.file_label
        assert file_label is not None
        assert "test.txt" in file_label.text()

    def test_update_statistics(self, progress_dialog):
        """测试统计信息更新"""
        summary = {
            "total": 10,
            "success": 5,
            "failed": 2,
            "skipped": 3,
        }
        progress_dialog.update_statistics(summary)

        # 验证统计标签已更新
        stats_label = progress_dialog.statistics_label
        assert stats_label is not None
        assert "总计: 10" in stats_label.text()

    def test_close_event(self, progress_dialog):
        """测试关闭事件"""
        progress_dialog.closeEvent(None)
        # 验证窗口已关闭

    def test_full_workflow(self, progress_dialog):
        """测试完整工作流程"""
        # 更新进度
        for i in range(1, 11):
            progress_dialog.update_progress(i, 10, f"file_{i}.txt")

        # 更新统计
        summary = {
            "total": 10,
            "success": 8,
            "failed": 1,
            "skipped": 1,
        }
        progress_dialog.update_statistics(summary)
