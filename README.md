# FileTypeTrans

一个基于 Python 的文件格式转换工具，能够将多种文档格式转换为 Markdown 格式。

## 功能特性

- ✅ **批量转换**: 递归遍历目录及其所有子目录
- ✅ **多种格式支持**: 文本、Word、PDF、Excel、PowerPoint
- ✅ **目录结构保持**: 在目标位置重建相同的目录结构
- ✅ **进度显示**: 实时显示转换进度和结果统计
- ✅ **智能过滤**: 自动跳过图片、代码、配置等不支持的文件
- ✅ **排除目录**: 自动排除 `.git`, `__pycache__`, `node_modules` 等目录
- ✅ **错误处理**: 完善的错误处理和日志记录

## 支持的文件格式

### 需要转换的文件

| 文件类型 | 扩展名 |
|----------|--------|
| 文本文件 | `.txt`, `.md`, `.rst`, `.adoc` |
| Word 文档 | `.docx`, `.doc` |
| Excel 表格 | `.xlsx`, `.xls`, `.csv` |
| PowerPoint | `.pptx`, `.ppt` |
| PDF 文档 | `.pdf` |

### 自动跳过的文件

| 文件类型 | 扩展名 |
|----------|--------|
| 图片文件 | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.svg`, `.webp`, `.ico` |
| 代码文件 | `.js`, `.ts`, `.java`, `.py`, `.c`, `.cpp`, `.h`, `.go`, `.rs`, `.html`, `.css` |
| 配置文件 | `.yaml`, `.yml`, `.xml`, `.json` |
| 压缩文件 | `.zip`, `.tar`, `.gz`, `.rar`, `.7z` |
| 可执行文件 | `.exe`, `.dmg`, `.app` |

### 自动排除的目录

- `.git`
- `__pycache__`
- `node_modules`
- `.venv`, `venv`, `env`
- `.env`
- `dist`, `build`
- `.pytest_cache`

## 安装

### 环境要求

- Python >= 3.10
- uv 包管理工具

### 安装步骤

```bash
# 1. 克隆仓库
git clone <repository-url>
cd FileTypeTrans

# 2. 安装依赖
uv sync

# 3. 激活虚拟环境（可选）
source .venv/bin/activate
```

## 使用方法

### 基本使用

```bash
# 转换当前目录
uv run python src/main.py
```

### 高级使用

```python
from pathlib import Path
from src.main import FileTypeTransApp

# 创建应用实例
app = FileTypeTransApp(Path("/path/to/source/directory"))

# 设置目标目录（可选，默认为 Downloads 目录）
app.set_target_dir(Path("/path/to/output/directory"))

# 运行转换
result = app.run()

# 查看结果
print(f"总文件数: {result['total']}")
print(f"成功: {result['success']}")
print(f"失败: {result['failed']}")
print(f"跳过: {result['skipped']}")
```

## 运行测试

```bash
# 运行所有测试
uv run pytest tests/ -v

# 运行特定测试文件
uv run pytest tests/test_config.py -v

# 运行特定测试类
uv run pytest tests/test_config.py::TestConfig -v

# 运行特定测试方法
uv run pytest tests/test_config.py::TestConfig::test_default_config -v
```

## 查看测试覆盖率

```bash
# 终端输出覆盖率
uv run pytest tests/ --cov=src --cov-report=term-missing

# 生成 HTML 覆盖率报告
uv run pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html

# 生成 XML 覆盖率报告
uv run pytest tests/ --cov=src --cov-report=xml
```

## 项目结构

```
FileTypeTrans/
├── src/
│   ├── main.py                    # 主控制器
│   ├── config/
│   │   ├── config.py             # 配置管理
│   │   └── constants.py          # 常量定义
│   ├── core/
│   │   ├── traversal.py          # 目录遍历器
│   │   ├── converter.py          # 转换器注册表
│   │   ├── file_handler.py       # 文件处理
│   │   └── converters/
│   │       ├── text_converter.py   # 文本转换器
│   │       ├── docx_converter.py  # Word 转换器
│   │       ├── pdf_converter.py   # PDF 转换器
│   │       ├── excel_converter.py  # Excel 转换器
│   │       └── pptx_converter.py  # PPT 转换器
│   ├── ui/
│   │   ├── cli.py               # 命令行界面
│   │   └── progress.py          # 进度显示
│   └── utils/
│       ├── logger.py            # 日志记录
│       └── exceptions.py        # 异常处理
├── tests/
│   ├── test_constants.py
│   ├── test_config.py
│   ├── test_traversal.py
│   ├── test_file_handler.py
│   ├── test_converter.py
│   ├── test_text_converter.py
│   ├── test_docx_converter.py
│   ├── test_pdf_converter.py
│   ├── test_excel_converter.py
│   ├── test_pptx_converter.py
│   ├── test_progress.py
│   ├── test_cli.py
│   ├── test_main.py
│   ├── test_logger.py
│   └── test_exceptions.py
├── pyproject.toml
├── README.md
├── CLAUDE.md
├── PRD.md
├── PROJECT_PROCESS.md
├── TEST_CASES.md
└── CODE_REVIEW.md
```

## 开发文档

- [PRD.md](PRD.md) - 产品需求文档
- [PROJECT_PROCESS.md](PROJECT_PROCESS.md) - 项目开发过程文档
- [TEST_CASES.md](TEST_CASES.md) - 测试用例文档
- [CODE_REVIEW.md](CODE_REVIEW.md) - 代码审查报告

## 技术栈

| 技术 | 版本 | 用途 |
|------|--------|------|
| Python | >= 3.10 | 编程语言 |
| uv | 最新 | 包管理工具 |
| python-docx | >= 0.8.11 | Word 文档处理 |
| PyPDF2 | >= 3.0.0 | PDF 文档处理 |
| pandas | >= 2.0.0 | Excel 表格处理 |
| openpyxl | >= 3.1.0 | Excel 读写 |
| python-pptx | >= 0.6.21 | PowerPoint 处理 |
| xlrd | >= 2.0.1 | 旧版 Excel 读取 |
| tqdm | >= 4.64.0 | 进度条显示 |
| pytest | >= 9.0.2 | 测试框架 |

## 许可证

本项目采用 GPL v3 开源协议。

## 贡献

欢迎贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 Issue
- 发起 Pull Request

---

**当前版本**: 0.1.0
**最后更新**: 2026-02-22
