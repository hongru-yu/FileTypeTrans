"""
主窗口模块 - 图形用户界面主入口
"""
import sys
from pathlib import Path
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox
)
from PyQt5.QtCore import Qt

from .worker import Worker
from .progress_dialog import ProgressDialog
from .result_dialog import ResultDialog
from src.main import FileTypeTransApp


class MainWindow(QMainWindow):
    """主窗口类"""

    def __init__(self, parent=None):
        """初始化主窗口"""
        super().__init__(parent)
        self.setWindowTitle("FileTypeTrans - 文件格式转换工具")
        self.setMinimumSize(800, 400)

        # 初始化应用
        self.app = None
        self.worker = None
        self.progress_dialog = None

        self._setup_ui()

    def _setup_ui(self):
        """设置界面布局"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setSpacing(20)

        # 标题
        title_label = QLabel("文件格式转换工具")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        layout.addWidget(title_label)

        # 描述
        desc_label = QLabel("将各种文档格式转换为 Markdown 格式")
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setStyleSheet("font-size: 14px; margin: 10px;")
        layout.addWidget(desc_label)

        # 源目录选择区域
        source_layout = self._create_directory_selector("源目录:", self._select_source_directory)
        self.source_input = source_layout.input_field
        layout.addLayout(source_layout)

        # 目标目录选择区域
        target_layout = self._create_directory_selector("目标目录:", self._select_target_directory)
        self.target_input = target_layout.input_field
        layout.addLayout(target_layout)

        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.convert_button = QPushButton("开始转换")
        self.convert_button.setMinimumWidth(200)
        self.convert_button.setMinimumHeight(50)
        self.convert_button.setStyleSheet(
            "font-size: 16px; font-weight: bold; "
            "background-color: #1976d2; color: white; "
            "border-radius: 5px; padding: 10px;"
        )
        self.convert_button.clicked.connect(self._on_convert_clicked)
        button_layout.addWidget(self.convert_button)

        button_layout.addStretch()
        layout.addLayout(button_layout)

        layout.addStretch()
        central_widget.setLayout(layout)

    def _create_directory_selector(self, label_text: str, slot_func):
        """创建目录选择器

        Args:
            label_text: 标签文本
            slot_func: 选择目录的槽函数

        Returns:
            QHBoxLayout: 布局对象
        """
        layout = QHBoxLayout()

        label = QLabel(label_text)
        label.setMinimumWidth(80)
        layout.addWidget(label)

        input_field = QLineEdit()
        input_field.setPlaceholderText("选择目录...")
        input_field.setReadOnly(True)
        layout.addWidget(input_field)

        button = QPushButton("浏览...")
        button.clicked.connect(slot_func)
        layout.addWidget(button)

        # 将输入字段添加到布局对象中，方便后续访问
        layout.input_field = input_field

        return layout

    def _select_source_directory(self):
        """选择源目录"""
        directory = QFileDialog.getExistingDirectory(
            self, "选择源目录", ""
        )
        if directory:
            self.source_input.setText(directory)

    def _select_target_directory(self):
        """选择目标目录"""
        directory = QFileDialog.getExistingDirectory(
            self, "选择目标目录", ""
        )
        if directory:
            self.target_input.setText(directory)

    def _on_convert_clicked(self):
        """处理转换按钮点击事件"""
        source_dir = self.source_input.text()
        target_path = self.target_input.text()

        # 验证输入
        if not source_dir:
            QMessageBox.warning(self, "警告", "请选择源目录！")
            return

        if not target_path:
            QMessageBox.warning(self, "警告", "请选择目标目录！")
            return

        if not Path(source_dir).exists():
            QMessageBox.warning(self, "警告", "源目录不存在！")
            return

        if not Path(target_path).exists():
            QMessageBox.warning(self, "警告", "目标目录不存在！")
            return

        # 开始转换
        self._start_conversion(source_dir, target_path)

    def _start_conversion(self, source_dir: str, target_path: str):
        """开始文件转换

        Args:
            source_dir: 源目录
            target_path: 目标路径
        """
        # 创建应用实例
        self.app = FileTypeTransApp(Path(source_dir), Path(target_path))

        # 创建并显示进度对话框
        self.progress_dialog = ProgressDialog(self)
        self.progress_dialog.show()

        # 创建工作线程
        self.worker = Worker(source_dir, target_path, self.app)
        self.worker.progress_updated.connect(self.progress_dialog.update_progress)
        self.worker.finished.connect(self._on_conversion_finished)
        self.worker.error_occurred.connect(self._on_conversion_error)
        self.worker.start()

    def _on_conversion_finished(self, summary: dict):
        """转换完成处理

        Args:
            summary: 统计信息
        """
        # 更新进度对话框的统计信息
        self.progress_dialog.update_statistics(summary)

        # 显示结果对话框
        target_path = self.target_input.text()
        result_dialog = ResultDialog(summary, target_path, self)
        result_dialog.exec_()

    def _on_conversion_error(self, error_message: str):
        """转换错误处理

        Args:
            error_message: 错误消息
        """
        QMessageBox.critical(self, "错误", f"转换过程中发生错误:\n{error_message}")
        if self.progress_dialog:
            self.progress_dialog.close()


def main():
    """主函数"""
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    # 设置应用样式
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
