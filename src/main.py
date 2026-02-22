"""
主控制器模块
"""
from pathlib import Path
from typing import Dict, Optional

from config.config import Config
from core.traversal import DirectoryTraversal
from core.converter import get_converter
from core.file_handler import FileHandler
from ui.progress import ProgressTracker


class FileTypeTransApp:
    """文件类型转换应用类"""

    def __init__(self, source_dir: Path):
        """
        初始化应用

        Args:
            source_dir: 源目录路径
        """
        self.source_dir = source_dir
        self.target_dir: Optional[Path] = None
        self.config = Config()
        self.file_handler = FileHandler()
        self.traversal = DirectoryTraversal(source_dir, self.config)

    def set_target_dir(self, target_dir: Path) -> None:
        """
        设置目标目录

        Args:
            target_dir: 目标目录路径
        """
        self.target_dir = target_dir

    def run(self) -> Dict[str, int]:
        """
        运行转换流程

        Returns:
            转换结果字典
        """
        # 确保目标目录设置
        if self.target_dir is None:
            # 使用默认的 Downloads 目录
            downloads_dir = Path.home() / "Downloads"
            target_dir = downloads_dir / self.source_dir.name
            self.target_dir = target_dir

        # 创建目标目录
        self.target_dir.mkdir(parents=True, exist_ok=True)

        # 收集所有文件
        files = list(self.traversal.collect_files())
        total_files = self.traversal.total_files
        supported_files = self.traversal.supported_files

        # 初始化进度跟踪器
        progress = ProgressTracker(total=total_files)

        # 转换文件
        success_count = 0
        failed_count = 0

        for file_path in files:
            try:
                self._convert_file(file_path)
                success_count += 1
                progress.increment_success()
            except Exception as e:
                failed_count += 1
                progress.increment_failed()
                print(f"转换失败: {file_path} - {e}")

            progress.increment_processed()

        return {
            "total": total_files,
            "success": success_count,
            "failed": failed_count,
            "skipped": total_files - supported_files,
        }

    def _convert_file(self, file_path: Path) -> None:
        """
        转换单个文件

        Args:
            file_path: 文件路径
        """
        # 获取对应的转换器
        converter = get_converter(file_path)

        if converter is None:
            raise ValueError(f"没有找到对应的转换器: {file_path}")

        # 转换文件
        markdown_content = converter.convert(file_path)

        # 获取相对路径
        relative_path = file_path.relative_to(self.source_dir)

        # 构建目标文件路径
        target_file_path = self.target_dir / relative_path
        target_file_path = target_file_path.with_suffix(".md")

        # 写入转换后的文件
        self.file_handler.write_file_content(target_file_path, markdown_content)


def main():
    """主函数"""
    # 创建应用实例
    app = FileTypeTransApp(Path.cwd())

    # 运行转换
    result = app.run()

    # 显示结果
    print(f"\n转换完成!")
    print(f"总文件数: {result['total']}")
    print(f"成功: {result['success']}")
    print(f"失败: {result['failed']}")
    print(f"跳过: {result['skipped']}")


if __name__ == "__main__":
    main()
