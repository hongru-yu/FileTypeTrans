"""
文件处理模块的单元测试
"""
import pytest
from pathlib import Path
from src.core.file_handler import FileHandler


class TestFileHandler:
    """测试文件处理类"""

    def test_read_file_content(self, tmp_path):
        """测试读取文件内容"""
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, World!")

        handler = FileHandler()
        content = handler.read_file_content(test_file)

        assert content == "Hello, World!"

    def test_read_nonexistent_file(self, tmp_path):
        """测试读取不存在的文件"""
        nonexistent_file = tmp_path / "nonexistent.txt"

        handler = FileHandler()

        with pytest.raises(FileNotFoundError):
            handler.read_file_content(nonexistent_file)

    def test_write_file_content(self, tmp_path):
        """测试写入文件内容"""
        test_file = tmp_path / "output.md"
        content = "# Markdown Content\n\nThis is a test."

        handler = FileHandler()
        handler.write_file_content(test_file, content)

        assert test_file.exists()
        assert test_file.read_text() == content

    def test_create_directory_structure(self, tmp_path):
        """测试创建目录结构"""
        # 创建相对路径
        relative_path = Path("subdir1/subdir2/file.md")

        handler = FileHandler()
        handler.create_directory_structure(tmp_path, relative_path)

        # 检查目录是否创建
        assert (tmp_path / "subdir1").exists()
        assert (tmp_path / "subdir1" / "subdir2").exists()

    def test_reproduce_directory_structure(self, tmp_path):
        """测试重建目录结构"""
        # 创建源目录结构
        source_dir = tmp_path / "source"
        source_dir.mkdir()
        file1 = source_dir / "file1.txt"
        file1.write_text("File 1")

        subdir = source_dir / "subdir"
        subdir.mkdir()
        file2 = subdir / "file2.txt"
        file2.write_text("File 2")

        # 创建目标目录
        target_dir = tmp_path / "target"

        handler = FileHandler()

        # 重建目录结构并获取目标路径
        target_file1 = handler.reproduce_directory_structure(source_dir, target_dir, file1)
        target_file2 = handler.reproduce_directory_structure(source_dir, target_dir, file2)

        # 检查返回的路径是否正确
        assert target_file1 == target_dir / "file1.txt"
        assert target_file2 == target_dir / "subdir" / "file2.txt"

        # 检查目录结构是否创建
        assert (target_dir).exists()
        assert (target_dir / "subdir").exists()

    def test_get_relative_path(self, tmp_path):
        """测试获取相对路径"""
        base_dir = tmp_path / "base"
        target_file = tmp_path / "base" / "subdir" / "file.txt"

        # 创建文件以确保存在
        target_file.parent.mkdir(parents=True)
        target_file.touch()

        handler = FileHandler()
        relative_path = handler.get_relative_path(base_dir, target_file)

        assert relative_path == Path("subdir/file.txt")

    def test_is_markdown_file(self):
        """测试判断是否为 Markdown 文件"""
        handler = FileHandler()

        assert handler.is_markdown_file(Path("test.md"))
        assert handler.is_markdown_file(Path("document.md"))
        assert not handler.is_markdown_file(Path("test.txt"))
        assert not handler.is_markdown_file(Path("test.pdf"))

    def test_convert_to_markdown_filename(self):
        """测试转换为 Markdown 文件名"""
        handler = FileHandler()

        assert handler.convert_to_markdown_filename(Path("test.txt")) == "test.md"
        assert handler.convert_to_markdown_filename(Path("document.pdf")) == "document.md"
        assert handler.convert_to_markdown_filename(Path("spreadsheet.xlsx")) == "spreadsheet.md"
        assert handler.convert_to_markdown_filename(Path("presentation.pptx")) == "presentation.md"
