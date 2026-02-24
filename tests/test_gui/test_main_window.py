"""
主窗口模块的单元测试
"""
import pytest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QLineEdit, QPushButton


class TestMainWindow:
    """测试主窗口"""

    @pytest.fixture
    def qapp(self, qapp):
        """确保 QApplication 实例存在"""
        return qapp

    @pytest.fixture
    def main_window(self, qapp):
        from src.ui.gui.main_window import MainWindow
        return MainWindow()

    def test_initialization(self, main_window):
        """测试初始化"""
        assert main_window is not None
        assert main_window.windowTitle() == "FileTypeTrans - 文件格式转换工具"

    def test_ui_elements_exist(self, main_window):
        """测试界面元素存在"""
        # 验证源目录选择器
        assert main_window.source_input is not None
        assert isinstance(main_window.source_input, QLineEdit)

        # 验证目标目录选择器
        assert main_window.target_input is not None
        assert isinstance(main_window.target_input, QLineEdit)

        # 验证转换按钮
        assert main_window.convert_button is not None
        assert isinstance(main_window.convert_button, QPushButton)

    def test_source_directory_selection(self, main_window):
        """测试源目录选择"""
        # 测试设置源目录
        test_path = "/test/source"
        main_window.source_input.setText(test_path)
        assert main_window.source_input.text() == test_path

    def test_target_directory_selection(self, main_window):
        """测试目标目录选择"""
        # 测试设置目标目录
        test_path = "/test/target"
        main_window.target_input.setText(test_path)
        assert main_window.target_input.text() == test_path

    def test_button_initial_state(self, main_window):
        """测试按钮初始状态"""
        # 转换按钮应该在开始时可用
        assert main_window.convert_button.isEnabled()
