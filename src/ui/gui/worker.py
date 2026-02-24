"""
后台工作线程模块 - 执行文件转换任务
"""
from PyQt5.QtCore import QThread, pyqtSignal


class Worker(QThread):
    """后台工作线程，执行文件转换任务"""

    # 信号定义
    progress_updated = pyqtSignal(int, int, str)  # current, total, filename
    finished = pyqtSignal(dict)  # summary
    error_occurred = pyqtSignal(str)  # error_message

    def __init__(self, source_dir: str, target_path: str, app, parent=None):
        """初始化工作线程

        Args:
            source_dir: 源目录
            target_path: 目标路径
            app: 文件转换应用对象
            parent: 父对象
        """
        super().__init__(parent)
        self.source_dir = source_dir
        self.target_path = target_path
        self.app = app

    def run(self):
        """执行文件转换任务"""
        try:
            # 执行转换
            summary = self.app.run()

            # 发送完成信号
            self.finished.emit(summary)

        except Exception as e:
            # 发送错误信号
            self.error_occurred.emit(str(e))

    def update_progress(self, current: int, total: int, filename: str):
        """更新进度

        Args:
            current: 当前处理的文件索引
            total: 文件总数
            filename: 当前处理的文件名
        """
        self.progress_updated.emit(current, total, filename)
