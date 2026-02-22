"""
主控制器模块的单元测试
"""
import pytest
from pathlib import Path
from src.main import FileTypeTransApp
from src.config.config import Config


class TestFileTypeTransApp:
    """测试主应用类"""

    def test_initialization(self, tmp_path):
        """测试初始化"""
        app = FileTypeTransApp(tmp_path)

        assert app.source_dir == tmp_path
        assert isinstance(app.config, Config)

    def test_set_target_dir(self, tmp_path):
        """测试设置目标目录"""
        app = FileTypeTransApp(tmp_path)

        target_dir = tmp_path / "output"
        app.set_target_dir(target_dir)

        assert app.target_dir == target_dir

    def test_run_without_target_dir(self, tmp_path):
        """测试没有设置目标目录时运行"""
        app = FileTypeTransApp(tmp_path)

        # 应该自动设置目标目录
        app.run()

        assert app.target_dir is not None

    def test_run_with_files(self, tmp_path):
        """测试运行转换"""
        # 创建测试文件
        (tmp_path / "test.txt").write_text("Hello World")

        target_dir = tmp_path / "output"

        app = FileTypeTransApp(tmp_path)
        app.set_target_dir(target_dir)

        result = app.run()

        assert result["total"] >= 1
        assert result["success"] >= 0
        assert target_dir.exists()
        assert (target_dir / "test.md").exists()

    def test_run_with_subdirectories(self, tmp_path):
        """测试运行转换包含子目录"""
        # 创建测试文件
        (tmp_path / "main.txt").write_text("Main file")

        subdir = tmp_path / "subdir"
        subdir.mkdir()
        (subdir / "sub.txt").write_text("Sub file")

        target_dir = tmp_path / "output"

        app = FileTypeTransApp(tmp_path)
        app.set_target_dir(target_dir)

        result = app.run()

        assert result["total"] >= 2
        assert (target_dir / "main.md").exists()
        assert (target_dir / "subdir" / "sub.md").exists()

    def test_run_with_mixed_files(self, tmp_path):
        """测试运行转换混合文件类型"""
        # 创建支持的文件
        (tmp_path / "test.txt").write_text("Hello")

        # 创建跳过的文件
        (tmp_path / "image.png").touch()

        target_dir = tmp_path / "output"

        app = FileTypeTransApp(tmp_path)
        app.set_target_dir(target_dir)

        result = app.run()

        # 应该只转换支持的文件
        assert (target_dir / "test.md").exists()
