"""
配置管理模块的单元测试
"""
import pytest
from pathlib import Path
from src.config.config import Config
from src.config.constants import (
    ALL_SUPPORTED_EXTENSIONS,
    EXCLUDED_DIRECTORIES,
    DEFAULT_DOWNLOAD_DIR,
)


class TestConfig:
    """测试配置类"""

    def test_default_config(self):
        """测试默认配置"""
        config = Config()
        assert config.supported_extensions == ALL_SUPPORTED_EXTENSIONS
        assert config.excluded_directories == EXCLUDED_DIRECTORIES
        assert config.download_dir == default_downloads_dir()

    def test_custom_config(self, tmp_path):
        """测试自定义配置"""
        custom_download = tmp_path / "custom_output"
        custom_extensions = {".txt", ".md"}
        custom_excluded = {".git", "temp"}

        config = Config(
            download_dir=custom_download,
            supported_extensions=custom_extensions,
            excluded_directories=custom_excluded,
        )

        assert config.download_dir == custom_download
        assert config.supported_extensions == custom_extensions
        assert config.excluded_directories == custom_excluded

    def test_is_supported_extension(self):
        """测试判断扩展名是否支持"""
        config = Config()

        # 支持的扩展名
        assert config.is_supported_extension(".txt")
        assert config.is_supported_extension(".pdf")
        assert config.is_supported_extension(".docx")

        # 不支持的扩展名
        assert not config.is_supported_extension(".png")
        assert not config.is_supported_extension(".js")
        assert not config.is_supported_extension(".unknown")

    def test_is_excluded_directory(self):
        """测试判断目录是否被排除"""
        config = Config()

        # 排除的目录
        assert config.is_excluded_directory(".git")
        assert config.is_excluded_directory("__pycache__")
        assert config.is_excluded_directory("node_modules")

        # 不排除的目录
        assert not config.is_excluded_directory("src")
        assert not config.is_excluded_directory("tests")
        assert not config.is_excluded_directory("docs")

    def test_should_process_file(self):
        """测试判断文件是否应该处理"""
        config = Config()

        # 应该处理的文件
        assert config.should_process_file("test.txt")
        assert config.should_process_file("document.pdf")

        # 不应该处理的文件
        assert not config.should_process_file("image.png")
        assert not config.should_process_file("script.js")
        assert not config.should_process_file("data.yml")

    def test_should_process_directory(self):
        """测试判断目录是否应该处理"""
        config = Config()

        # 应该处理的目录
        assert config.should_process_directory("src")
        assert config.should_process_directory("docs")

        # 不应该处理的目录
        assert not config.should_process_directory(".git")
        assert not config.should_process_directory("__pycache__")


def default_downloads_dir():
    """获取默认下载目录"""
    home = Path.home()
    return home / DEFAULT_DOWNLOAD_DIR


class TestConfigFileHandling:
    """测试配置文件处理"""

    def test_create_download_dir(self, tmp_path):
        """测试创建下载目录"""
        download_dir = tmp_path / "downloads"
        config = Config(download_dir=download_dir)

        # 目录不存在时创建
        assert not download_dir.exists()
        config.ensure_download_dir()
        assert download_dir.exists()
        assert download_dir.is_dir()

    def test_download_dir_already_exists(self, tmp_path):
        """测试下载目录已存在的情况"""
        download_dir = tmp_path / "downloads"
        download_dir.mkdir()

        config = Config(download_dir=download_dir)
        config.ensure_download_dir()

        # 目录应该仍然存在
        assert download_dir.exists()
        assert download_dir.is_dir()
