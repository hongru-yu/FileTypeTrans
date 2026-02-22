"""
日志记录模块的单元测试
"""
import pytest
import tempfile
import os
from src.utils.logger import Logger


class TestLogger:
    """测试日志类"""

    def test_initialization(self, tmp_path):
        """测试初始化"""
        log_file = tmp_path / "test.log"
        logger = Logger(log_file)

        assert logger.log_file == log_file

    def test_info(self, tmp_path):
        """测试信息日志"""
        log_file = tmp_path / "test.log"
        logger = Logger(log_file)

        logger.info("测试信息")

        assert log_file.exists()
        content = log_file.read_text()
        assert "测试信息" in content
        assert "INFO" in content

    def test_warning(self, tmp_path):
        """测试警告日志"""
        log_file = tmp_path / "test.log"
        logger = Logger(log_file)

        logger.warning("测试警告")

        assert log_file.exists()
        content = log_file.read_text()
        assert "测试警告" in content
        assert "WARNING" in content

    def test_error(self, tmp_path):
        """测试错误日志"""
        log_file = tmp_path / "test.log"
        logger = Logger(log_file)

        logger.error("测试错误")

        assert log_file.exists()
        content = log_file.read_text()
        assert "测试错误" in content
        assert "ERROR" in content

    def test_multiple_logs(self, tmp_path):
        """测试多条日志"""
        log_file = tmp_path / "test.log"
        logger = Logger(log_file)

        logger.info("信息1")
        logger.warning("警告1")
        logger.error("错误1")

        content = log_file.read_text()
        assert "信息1" in content
        assert "警告1" in content
        assert "错误1" in content
