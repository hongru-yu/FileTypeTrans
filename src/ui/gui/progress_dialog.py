"""
进度对话框模块 - 显示文件转换进度
"""
from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton
)
from PyQt5.QtCore import Qt


class ProgressDialog(QDialog):
    """显示文件转换进度的对话框"""

    def __init__(self, parent=None):
        """初始化进度对话框"""
        super().__init__(parent)
        self.setWindowTitle("文件转换进度")
        self.setModal(True)
        self.setMinimumWidth(500)

        self._setup_ui()

    def _setup_ui(self):
        """设置界面布局"""
        layout = QVBoxLayout()

        # 标题
        title_label = QLabel("正在转换文件...")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(title_label)

        # 文件名标签
        self.file_label = QLabel("准备中...")
        self.file_label.setAlignment(Qt.AlignCenter)
        self.file_label.setStyleSheet("font-size: 14px; margin: 10px;")
        layout.addWidget(self.file_label)

        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # 统计标签
        self.statistics_label = QLabel("统计: 等待开始...")
        self.statistics_label.setAlignment(Qt.AlignCenter)
        self.statistics_label.setStyleSheet("font-size: 12px; margin: 10px;")
        layout.addWidget(self.statistics_label)

        # 关闭按钮（初始禁用）
        self.close_button = QPushButton("关闭")
        self.close_button.setEnabled(False)
        self.close_button.clicked.connect(self.close)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.close_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def update_progress(self, current: int, total: int, filename: str):
        """更新进度信息

        Args:
            current: 当前处理的文件索引
            total: 文件总数
            filename: 当前处理的文件名
        """
        self.file_label.setText(f"正在处理: {filename}")

        # 更新进度条
        if total > 0:
            progress = int((current / total) * 100)
            self.progress_bar.setValue(progress)
            self.progress_bar.setFormat(f"{current}/{total} (%p%)")

        # 禁用关闭按钮（转换进行中）
        self.close_button.setEnabled(False)

    def update_statistics(self, summary: dict):
        """更新统计信息

        Args:
            summary: 统计信息字典，包含:
                - total: 总文件数
                - success: 成功数
                - failed: 失败数
                - skipped: 跳过数
        """
        total = summary.get("total", 0)
        success = summary.get("success", 0)
        failed = summary.get("failed", 0)
        skipped = summary.get("skipped", 0)

        stats_text = (
            f"总计: {total} | "
            f"成功: {success} | "
            f"失败: {failed} | "
            f"跳过: {skipped}"
        )
        self.statistics_label.setText(stats_text)

        # 转换完成，启用关闭按钮
        self.progress_bar.setValue(100)
        self.close_button.setEnabled(True)
        self.file_label.setText("转换完成！")

    def closeEvent(self, event):
        """处理关闭事件"""
        # 只有在转换完成后才允许关闭
        if self.close_button.isEnabled():
            super().closeEvent(event)
        elif event is not None:
            event.ignore()
