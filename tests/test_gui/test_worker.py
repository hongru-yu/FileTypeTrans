"""
后台工作线程模块的单元测试
"""
import pytest
from unittest.mock import MagicMock, patch
from PyQt5.QtCore import pyqtSignal


class TestWorker:
    """测试后台工作线程"""

    @pytest.fixture
    def qapp(self, qapp):
        """确保 QApplication 实例存在"""
        return qapp

    @pytest.fixture
    def mock_app(self):
        """模拟应用对象"""
        app = MagicMock()
        app.run.return_value = {
            "total": 10,
            "success": 8,
            "failed": 1,
            "skipped": 1,
        }
        return app

    @pytest.fixture
    def worker(self, qapp, mock_app):
        from src.ui.gui.worker import Worker
        worker = Worker("/src", "/dst", mock_app)
        return worker

    def test_initialization(self, worker):
        """测试初始化"""
        assert worker is not None
        assert worker.source_dir == "/src"
        assert worker.target_path == "/dst"

    def test_signal_definitions(self, worker):
        """测试信号定义"""
        # 验证信号存在
        assert hasattr(worker, "progress_updated")
        assert hasattr(worker, "finished")
        assert hasattr(worker, "error_occurred")

    def test_run_success(self, worker):
        """测试成功运行"""
        worker.run()
        # 验证应用运行方法被调用
        worker.app.run.assert_called_once()

    def test_finished_signal(self, worker):
        """测试完成信号"""
        # 连接信号到槽
        finished_called = []

        def on_finished(summary):
            finished_called.append(summary)

        worker.finished.connect(on_finished)
        worker.run()

        # 验证信号已触发
        assert len(finished_called) == 1
        assert finished_called[0]["total"] == 10
