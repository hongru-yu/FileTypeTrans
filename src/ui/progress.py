"""
进度显示模块
"""
from tqdm import tqdm


class ProgressTracker:
    """进度跟踪器"""

    def __init__(self, total: int):
        """
        初始化进度跟踪器

        Args:
            total: 总文件数量
        """
        self.total = total
        self.processed = 0
        self.success = 0
        self.failed = 0
        self.skipped = 0
        self._progress_bar = None

    def increment_processed(self, count: int = 1) -> None:
        """
        增加已处理文件数量

        Args:
            count: 增加的数量
        """
        self.processed += count

    def increment_success(self, count: int = 1) -> None:
        """
        增加成功文件数量

        Args:
            count: 增加的数量
        """
        self.success += count

    def increment_failed(self, count: int = 1) -> None:
        """
        增加失败文件数量

        Args:
            count: 增加的数量
        """
        self.failed += count

    def increment_skipped(self, count: int = 1) -> None:
        """
        增加跳过文件数量

        Args:
            count: 增加的数量
        """
        self.skipped += count

    def get_percentage(self) -> float:
        """
        获取进度百分比

        Returns:
            进度百分比 (0.0 - 100.0)
        """
        if self.total == 0:
            return 0.0
        return (self.processed / self.total) * 100.0

    def is_complete(self) -> bool:
        """
        判断是否完成

        Returns:
            是否完成
        """
        return self.processed >= self.total

    def get_summary(self) -> str:
        """
        获取摘要信息

        Returns:
            摘要字符串
        """
        return f"总数: {self.total}, 成功: {self.success}, 失败: {self.failed}, 跳过: {self.skipped}"
