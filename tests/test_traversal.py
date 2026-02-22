"""
目录遍历模块的单元测试
"""
import pytest
from pathlib import Path
from src.core.traversal import DirectoryTraversal
from src.config.config import Config


class TestDirectoryTraversal:
    """测试目录遍历类"""

    def test_collect_files_empty_directory(self, tmp_path):
        """测试空目录"""
        config = Config()
        traversal = DirectoryTraversal(tmp_path, config)

        files = list(traversal.collect_files())

        assert len(files) == 0
        assert traversal.total_files == 0
        assert traversal.supported_files == 0
        assert traversal.skipped_files == 0

    def test_collect_files_with_supported_files(self, tmp_path):
        """测试收集支持的文件"""
        # 创建支持的文件
        (tmp_path / "test.txt").write_text("Hello World")
        (tmp_path / "document.pdf").touch()
        (tmp_path / "spreadsheet.xlsx").touch()

        config = Config()
        traversal = DirectoryTraversal(tmp_path, config)

        files = list(traversal.collect_files())

        assert len(files) == 3
        assert traversal.total_files == 3
        assert traversal.supported_files == 3
        assert traversal.skipped_files == 0

    def test_collect_files_with_mixed_files(self, tmp_path):
        """测试混合文件类型"""
        # 创建支持的文件
        (tmp_path / "test.txt").write_text("Hello World")
        (tmp_path / "document.pdf").touch()

        # 创建跳过的文件
        (tmp_path / "image.png").touch()
        (tmp_path / "script.js").touch()

        config = Config()
        traversal = DirectoryTraversal(tmp_path, config)

        files = list(traversal.collect_files())

        assert len(files) == 2  # 只有支持的文件
        assert traversal.total_files == 4  # 总共4个文件
        assert traversal.supported_files == 2
        assert traversal.skipped_files == 2

    def test_collect_files_recursive_with_subdirectories(self, tmp_path):
        """测试递归遍历子目录"""
        # 创建主目录文件
        (tmp_path / "main.txt").write_text("Main file")

        # 创建子目录
        subdir = tmp_path / "subdir"
        subdir.mkdir()
        (subdir / "sub.txt").write_text("Sub file")

        # 创建嵌套子目录
        nested = subdir / "nested"
        nested.mkdir()
        (nested / "nested.txt").write_text("Nested file")

        config = Config()
        traversal = DirectoryTraversal(tmp_path, config)

        files = list(traversal.collect_files())

        assert len(files) == 3
        assert traversal.total_files == 3

    def test_collect_files_excludes_directories(self, tmp_path):
        """测试排除目录"""
        # 创建正常目录
        normal_dir = tmp_path / "normal"
        normal_dir.mkdir()
        (normal_dir / "test.txt").write_text("Normal file")

        # 创建排除目录
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "config").write_text("Git config")

        pycache_dir = tmp_path / "__pycache__"
        pycache_dir.mkdir()
        (pycache_dir / "test.pyc").touch()

        config = Config()
        traversal = DirectoryTraversal(tmp_path, config)

        files = list(traversal.collect_files())

        assert len(files) == 1
        assert files[0].name == "test.txt"

    def test_collect_files_returns_correct_paths(self, tmp_path):
        """测试返回正确的文件路径"""
        # 创建文件
        (tmp_path / "test.txt").write_text("Hello World")

        config = Config()
        traversal = DirectoryTraversal(tmp_path, config)

        files = list(traversal.collect_files())

        assert len(files) == 1
        assert files[0] == tmp_path / "test.txt"
        assert files[0].exists()

    def test_get_file_extension(self):
        """测试获取文件扩展名"""
        config = Config()
        traversal = DirectoryTraversal(Path("/tmp"), config)

        assert traversal.get_file_extension("test.txt") == ".txt"
        assert traversal.get_file_extension("document.pdf") == ".pdf"
        assert traversal.get_file_extension("image.png") == ".png"
        assert traversal.get_file_extension("no_extension") == ""
