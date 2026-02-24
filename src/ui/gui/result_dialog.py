"""
结果对话框模块 - 显示转换完成后的统计信息
"""
import subprocess
import platform
from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QWidget
)
from PyQt5.QtCore import Qt


class ResultDialog(QDialog):
    """显示转换完成结果的对话框"""

    def __init__(self, summary: dict, output_dir: str, parent=None):
        """初始化结果对话框

        Args:
            summary: 统计信息字典
            output_dir: 输出目录路径
            parent: 父窗口
        """
        super().__init__(parent)
        self.summary_data = summary
        self.output_dir = output_dir
        self.setWindowTitle("转换完成")
        self.setModal(True)
        self.setMinimumWidth(600)

        self._setup_ui()

    def _setup_ui(self):
        """设置界面布局"""
        layout = QVBoxLayout()

        # 标题
        title_label = QLabel("文件转换完成！")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px; color: #2e7d32;")
        layout.addWidget(title_label)

        # 统计信息内容
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setMaximumHeight(200)

        stats_widget = QWidget()
        stats_layout = QVBoxLayout()

        total = self.summary_data.get("total", 0)
        success = self.summary_data.get("success", 0)
        failed = self.summary_data.get("failed", 0)
        skipped = self.summary_data.get("skipped", 0)

        # 添加统计项
        stats_layout.addWidget(self._create_stat_label("总文件数", total))
        stats_layout.addWidget(self._create_stat_label("转换成功", success, color="#2e7d32"))
        stats_layout.addWidget(self._create_stat_label("转换失败", failed, color="#c62828"))
        stats_layout.addWidget(self._create_stat_label("跳过文件", skipped, color="#f57c00"))

        stats_layout.addStretch()
        stats_widget.setLayout(stats_layout)
        scroll_area.setWidget(stats_widget)
        layout.addWidget(scroll_area)

        # 输出目录
        output_label = QLabel(f"输出目录: {self.output_dir}")
        output_label.setStyleSheet("font-size: 12px; margin: 10px;")
        output_label.setWordWrap(True)
        layout.addWidget(output_label)

        # 按钮区域
        button_layout = QHBoxLayout()

        # 打开文件夹按钮
        self.open_button = QPushButton("打开输出文件夹")
        self.open_button.clicked.connect(self._open_output_folder)
        button_layout.addWidget(self.open_button)

        # 关闭按钮
        self.close_button = QPushButton("关闭")
        self.close_button.clicked.connect(self.close)
        button_layout.addWidget(self.close_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def _create_stat_label(self, text: str, value: int, color: str = "#1565c0") -> QLabel:
        """创建统计标签

        Args:
            text: 标签文本
            value: 统计值
            color: 颜色值

        Returns:
            QLabel: 统计标签对象
        """
        label = QLabel(f"{text}: {value}")
        label.setStyleSheet(f"font-size: 14px; margin: 5px; color: {color};")
        return label

    def _open_output_folder(self):
        """打开输出文件夹"""
        try:
            if platform.system() == "Windows":
                subprocess.run(["explorer", self.output_dir])
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", self.output_dir])
            else:  # Linux
                subprocess.run(["xdg-open", self.output_dir])
        except Exception as e:
            print(f"无法打开文件夹: {e}")
