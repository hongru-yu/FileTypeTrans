"""
配置管理模块
"""
from pathlib import Path
from dataclasses import dataclass, field
from typing import Set

from src.config.constants import (
    ALL_SUPPORTED_EXTENSIONS,
    EXCLUDED_DIRECTORIES,
    DEFAULT_DOWNLOAD_DIR,
)


@dataclass
class Config:
    """配置类"""

    # 下载目录
    download_dir: Path = field(
        default_factory=lambda: Path.home() / DEFAULT_DOWNLOAD_DIR
    )

    # 支持的文件扩展名
    supported_extensions: Set[str] = field(
        default_factory=lambda: ALL_SUPPORTED_EXTENSIONS.copy()
    )

    # 排除的目录
    excluded_directories: Set[str] = field(
        default_factory=lambda: EXCLUDED_DIRECTORIES.copy()
    )

    def is_supported_extension(self, extension: str) -> bool:
        """判断文件扩展名是否支持"""
        return extension.lower() in self.supported_extensions

    def is_excluded_directory(self, directory_name: str) -> bool:
        """判断目录是否被排除"""
        return directory_name in self.excluded_directories

    def should_process_file(self, file_path: str) -> bool:
        """判断文件是否应该处理"""
        path = Path(file_path)
        extension = path.suffix
        return self.is_supported_extension(extension)

    def should_process_directory(self, directory_name: str) -> bool:
        """判断目录是否应该处理"""
        return not self.is_excluded_directory(directory_name)

    def ensure_download_dir(self) -> None:
        """确保下载目录存在"""
        self.download_dir.mkdir(parents=True, exist_ok=True)
