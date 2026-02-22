"""
日志记录模块
"""
from pathlib import Path
from datetime import datetime


class Logger:
    """日志记录器"""

    def __init__(self, log_file: Path):
        """
        初始化日志记录器

        Args:
            log_file: 日志文件路径
        """
        self.log_file = log_file
        self._ensure_log_file()

    def _ensure_log_file(self) -> None:
        """确保日志文件存在"""
        if not self.log_file.exists():
            self.log_file.parent.mkdir(parents=True, exist_ok=True)
            self.log_file.touch()

    def _write_log(self, level: str, message: str) -> None:
        """
        写入日志

        Args:
            level: 日志级别
            message: 日志消息
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

    def info(self, message: str) -> None:
        """
        记录信息日志

        Args:
            message: 日志消息
        """
        self._write_log("INFO", message)

    def warning(self, message: str) -> None:
        """
        记录警告日志

        Args:
            message: 日志消息
        """
        self._write_log("WARNING", message)

    def error(self, message: str) -> None:
        """
        记录错误日志

        Args:
            message: 日志消息
        """
        self._write_log("ERROR", message)
