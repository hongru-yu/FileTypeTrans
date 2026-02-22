"""
文件处理模块
"""
from pathlib import Path


class FileHandler:
    """文件处理类"""

    @staticmethod
    def read_file_content(file_path: Path) -> str:
        """
        读取文件内容

        Args:
            file_path: 文件路径

        Returns:
            文件内容

        Raises:
            FileNotFoundError: 文件不存在
        """
        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        return file_path.read_text(encoding="utf-8", errors="ignore")

    @staticmethod
    def write_file_content(file_path: Path, content: str) -> None:
        """
        写入文件内容

        Args:
            file_path: 文件路径
            content: 要写入的内容
        """
        # 确保父目录存在
        file_path.parent.mkdir(parents=True, exist_ok=True)

        file_path.write_text(content, encoding="utf-8")

    @staticmethod
    def create_directory_structure(base_dir: Path, relative_path: Path) -> Path:
        """
        创建目录结构

        Args:
            base_dir: 基础目录
            relative_path: 相对路径

        Returns:
            完整的目标文件路径
        """
        target_path = base_dir / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        return target_path

    @staticmethod
    def reproduce_directory_structure(
        source_dir: Path, target_dir: Path, file_path: Path
    ) -> Path:
        """
        重建目录结构

        Args:
            source_dir: 源目录
            target_dir: 目标目录
            file_path: 文件路径

        Returns:
            目标文件路径
        """
        relative_path = file_path.relative_to(source_dir)
        target_path = target_dir / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        return target_path

    @staticmethod
    def get_relative_path(base_dir: Path, file_path: Path) -> Path:
        """
        获取相对路径

        Args:
            base_dir: 基础目录
            file_path: 文件路径

        Returns:
            相对路径
        """
        return file_path.relative_to(base_dir)

    @staticmethod
    def is_markdown_file(file_path: Path) -> bool:
        """
        判断是否为 Markdown 文件

        Args:
            file_path: 文件路径

        Returns:
            是否为 Markdown 文件
        """
        return file_path.suffix == ".md"

    @staticmethod
    def convert_to_markdown_filename(file_path: Path) -> str:
        """
        转换为 Markdown 文件名

        Args:
            file_path: 文件路径

        Returns:
            Markdown 文件名
        """
        return f"{file_path.stem}.md"
