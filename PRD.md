# 产品需求文档 (PRD) - FileTypeTrans

## 文档信息

| 项目 | 信息 |
|------|------|
| 项目名称 | FileTypeTrans |
| 文档版本 | v2.0 |
| 创建日期 | 2026-02-22 |
| 文档状态 | 已完成 |

---

## 1. 项目概述

### 1.1 项目简介
FileTypeTrans 是一个基于 Python 的文件格式转换工具，使用 uv 管理依赖。该工具能够递归遍历用户指定的源目录，将标准文档文件统一转换为 Markdown 格式，并在 Downloads 文件夹下重建相同的目录结构进行保存。

### 1.2 项目目标

- 提供简单易用的图形用户界面
- 支持主流文档格式的批量转换
- 保持原始目录结构
- 提供清晰的转换进度和结果反馈
- 完善的错误处理机制

---

## 2. 功能需求

### 2.1 核心功能

#### 2.1.1 目录遍历
- 递归遍历用户指定的源目录及其所有子目录
- 支持排除特定目录（如 .git, __pycache__, node_modules）
- 统计总文件数量和待转换文件数量

#### 2.1.2 文件类型识别
根据文件扩展名识别文件类型：
- 支持转换的文档文件
- 跳过的文件（图片、代码、二进制文件）
- 显示跳过原因

#### 2.1.3 文件格式转换
将支持的文档文件转换为 Markdown 格式

#### 2.1.4 目录结构重建
在 Downloads 文件夹下创建与源目录相同的目录结构

#### 2.1.5 进度显示
- 显示当前处理文件
- 显示处理进度（已处理/总数）
- 显示成功、跳过、失败的文件数量

### 2.2 图形用户界面需求

#### 2.2.1 界面功能
- 文件夹选择
  - 通过图形界面选择源文件夹
  - 通过图形界面选择目标文件夹（或使用默认）
- 实时进度显示
  - 转换完成后的结果统计
  - 支持直接打开目标文件夹

#### 2.2.2 交互模式
- 开始转换按钮
- 验证提示（目录是否存在、是否有权限）
- 错误处理
- 状态提示

#### 2.2.3 后台处理
- 使用独立线程进行文件转换，避免界面冻结
- 实时更新进度信号
- 支持取消转换操作

---

## 3. 支持的文件类型

### 3.1 需要转换的文件

| 文件类型 | �.扩展名文件 |
|----------|--------------|
| 文本文件 | .txt, .md, .rst, .adoc |
| Word 文档 | .docx, .doc |
| Excel 表格 | .xlsx, .xls, .csv |
| PowerPoint | .pptx, .ppt |
| PDF 文档 | .pdf |

### 3.2 不转换的文件

| 文件类型 | 扩展名文件 |
|----------|--------------|
| 图片文件 | .png, .jpg, .jpeg, .gif, .bmp, .svg, .webp, .ico |
| 代码文件 | .js, .ts, .java, .py, .c, .cpp, .h, .go, .rs, .html, .css |
| 配置文件 | .yaml, .yml, .xml, .json |
| 压缩文件 | .zip, .tar, .gz, .rar, .7z |
| 可执行文件 | .exe, .dmg, .app |

---

## 4. 技术设计

### 4.1 技术栈

| 技术 | 版本要求 | 用途 |
|------|----------|----------|
| Python | >= 3.10 | 编程语言 |
| uv | 最新 | 包管理工具 |
| PyQt5 | >= 5.15.9 | 图形用户界面框架 |

### 4.2 核心依赖

| 依赖库 | 版本要求 | 用途 |
|--------|----------|----------|
| python-docx | >= 0.8.11 | 处理 .docx 文件 |
| PyPDF2 | >= 3.0.0 | 处理 .pdf 文件 |
| pandas | >= 2.0.0 | 处理 .xlsx 和 .csv 文件 |
| openpyxl | >= 3.1.0 | 支持 pandas 读取 .xlsx |
| python-pptx | >= 0.6.21 | 处理 .pptx 文件 |
| xlrd | >= 2.0.1 | 处理 .xls 文件 |
| python-magic | >= 0.4.27 | 文件类型检测 |
| tqdm | >= 4.64.0 | 进度条显示 |
| click | >= 8.1.0 | 命令行接口 |
| rich | >= 13.4.0 | 富文本控制台显示 |
| pathspec | >= 0.11.0 | 路径匹配和排除 |

### 4.3 可选依赖

| 依赖库 | 版本要求 | 用途 |
|--------|----------|----------|
| pytest-qt | >= 4.2.0 | GUI 测试框架 |
| pytest | >= 9.0.2 | 核心测试框架 |
| pytest-cov | >= 4.1.0 | 覆盖率报告 |

---

## 5. 项目结构

```python
FileTypeTrans/
├── src/
│   ├── main.py                      # 主控制器
│   ├── config/
│   │   ├── config.py                # 配置管理
│   │   └── constants.py             # 常量定义
│   ├── core/
│   │   ├── traversal.py                   # 目录遍历器
│   │   ├── converter.py                   # 通用转换接口
│   │   ├── file_handler.py                # 文件读写和目录创建
│   │   └── converters/
│   │       ├── text_converter.py        # .txt, .md, .rst, .adoc
│   │       ├── docx_converter.py        # .docx, .doc
│   │       ├── pdf_converter.py          # .pdf
│   │       ├── excel_converter.py       # .xlsx, .xls, .csv
│   │       └── pptx_converter.py      # .pptx, .ppt
│   ├── ui/
│   │   ├── cli.py                         # 命令行界面
│   │   ├── progress.py                    # 进度显示
│   │   └── gui/                         # 图形用户界面
│   │       ├── __init__.py
│   │       ├── main_window.py         # 主窗口
│   │       ├── worker.py            # 后台工作线程
│   │       ├── progress_dialog.py     # 进度对话框
│   │       └── result_dialog.py      # 结果对话框
│   └── utils/
│       ├── logger.py                     # 日志记录
│       └── exceptions.py                # 异常处理
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
│   ├── test_exceptions.py
│   └── test_gui/                    # GUI 测试
│       ├── test_constants.py
│       ├── test_main_window.py
│       ├── test_worker.py
│       ├── test_progress_dialog.py
│       └── test_result_dialog.py
├── pyproject.toml                       # 项目配置
├── README.md                              # 项目说明
└── PRD.md                                # 产品需求文档
```

---

## 6. 验收标准

### 6.1 功能验收
- 能够成功转换所有支持类型的文件
- 转换后的文件保持原有的目录结构
- 提供清晰的进度和结果反馈
- 图形界面响应灵敏，不阻塞
- 正确处理错误和异常情况
- 正确跳过不支持的文件

### 6.2 性能验收
- 转换 100 个文件的响应时间合理
- 内存占用在合理范围内
- 图形界面操作流畅

### 6.3 代码质量
- 代码符合 PEP 8 规范
- 所有公共函数都有文档字符串
- 所有公共类都有文档字符串
- 无 TODO/FIXME 注释

---

## 7. 开发计划

### 7.1 实施阶段
- 阶段 1: 项目基础架构搭建
- 阶段 2: 核心功能实现（目录遍历、文件处理、转换器）
- 阶段 3: 图形用户界面实现
- 阶段 4: 测试和文档编写
- 阶段 5: 集成测试和覆盖率验证

### 7.2 优先级
- 高优先级（立即开始）：
  - 项目基础架构
  - 核心转换功能（文本、Word、PDF）
  - 目录遍历和文件处理
- 中优先级：
  - Excel 和 PPT 文件转换
  - 进度显示和结果报告
  - 错误处理和容错
- 低优先级：
  - 性能优化
  - 高级配置选项

---

## 8. 文档维护

本文档应该随着项目的发展不断更新，包括：
- 新增功能
- 重大变更
-  Bug 修复
- 性能优化

---

*文档更新时间: 2026-02-22*
