"""
异常处理模块
"""


class ConversionError(Exception):
    """转换错误基类"""

    def __init__(self, message: str, file_path: str = ""):
        """
        初始化转换错误

        Args:
            message: 错误消息
            file_path: 文件路径（可选）
        """
        self.message = message
        self.file_path = file_path

        if file_path:
            super().__init__(f"{message} (文件: {file_path})")
        else:
            super().__init__(message)


class FileNotFoundError(ConversionError):
    """文件未找到错误"""

    def __init__(self, message: str):
        """
        初始化文件未找到错误

        Args:
            message: 错误消息
        """
        super().__init__(message)


class UnsupportedFormatError(ConversionError):
    """不支持格式错误"""

    def __init__(self, message: str, file_format: str = ""):
        """
        初始化不支持格式错误

        Args:
            message: 错误消息
            file_format: 文件格式（可选）
        """
        self.file_format = file_format

        if file_format:
            super().__init__(f"{message} (格式: {file_format})")
        else:
            super().__init__(message)
