"""
配置常量模块
定义支持的文件类型和排除规则
"""

# 支持转换的文件扩展名

# 文本文件
SUPPORTED_TEXT_EXTENSIONS = {".txt", ".md", ".rst", ".adoc"}

# Word 文档
SUPPORTED_DOCX_EXTENSIONS = {".docx", ".doc"}

# PDF 文档
SUPPORTED_PDF_EXTENSIONS = {".pdf"}

# Excel 表格
SUPPORTED_EXCEL_EXTENSIONS = {".xlsx", ".xls", ".csv"}

# PowerPoint 演示文稿
SUPPORTED_PPTX_EXTENSIONS = {".pptx", ".ppt"}

# 所有支持的扩展名
ALL_SUPPORTED_EXTENSIONS = (
    SUPPORTED_TEXT_EXTENSIONS
    | SUPPORTED_DOCX_EXTENSIONS
    | SUPPORTED_PDF_EXTENSIONS
    | SUPPORTED_EXCEL_EXTENSIONS
    | SUPPORTED_PPTX_EXTENSIONS
)

# 需要跳过的文件扩展名

# 图片文件
IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".svg",
    ".webp",
    ".ico",
}

# 代码文件
CODE_EXTENSIONS = {
    ".js",
    ".ts",
    ".java",
    ".py",
    ".c",
    ".cpp",
    ".h",
    ".go",
    ".rs",
    ".html",
    ".css",
    ".yaml",
    ".yml",
    ".xml",
    ".json",
}

# 配置文件
CONFIG_EXTENSIONS = {".yml"}

# 压缩文件
ARCHIVE_EXTENSIONS = {".zip", ".tar", ".gz", ".rar", ".7z"}

# 可执行文件
EXECUTABLE_EXTENSIONS = {".exe", ".dmg", ".app"}

# 所有跳过的扩展名
ALL_SKIPPED_EXTENSIONS = (
    IMAGE_EXTENSIONS
    | CODE_EXTENSIONS
    | CONFIG_EXTENSIONS
    | ARCHIVE_EXTENSIONS
    | EXECUTABLE_EXTENSIONS
)

# 需要排除的目录
EXCLUDED_DIRECTORIES = {
    ".git",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "env",
    ".env",
    "dist",
    "build",
    ".pytest_cache",
}

# 默认下载目录
DEFAULT_DOWNLOAD_DIR = "Downloads"
