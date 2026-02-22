# FileTypeTrans 测试用例文档

## 测试概览

| 指标 | 数值 |
|--------|------|
| 总测试数 | 154 |
| 通过率 | 100% |
| 代码覆盖率 | 93% |
| 测试框架 | pytest |
| Python 版本 | 3.10.14 |

---

## 测试模块分类

### 1. 配置相关测试 (22 个测试)

#### 测试文件
- `tests/test_constants.py` (14 个测试)
- `tests/test_config.py` (8 个测试)

#### 测试用例

##### test_constants.py

| 测试名称 | 描述 | 优先级 |
|----------|------|--------|
| test_supported_text_extensions | 测试支持的文本文件扩展名 | 高 |
| test_supported_docx_extensions | 测试支持的 Word 文档扩展名 | 高 |
| test_supported_pdf_extensions | 测试支持的 PDF 扩展名 | 高 |
| test_supported_excel_extensions | 测试支持的 Excel 扩展名 | 高 |
| test_supported_pptx_extensions | 测试支持的 PPT 扩展名 | 高 |
| test_all_supported_extensions | 测试所有支持的扩展名集合 | 高 |
| test_excluded_directories | 测试排除的目录 | 高 |
| test_image_extensions | 测试图片扩展名 | 中 |
| test_code_extensions | 测试代码文件扩展名 | 中 |
| test_config_extensions | 测试配置文件扩展名 | 中 |
| test_archive_extensions | 测试压缩文件扩展名 | 中 |
| test_executable_extensions | 测试可执行文件扩展名 | 中 |
| test_all_skipped_extensions | 测试所有跳过的扩展名集合 | 中 |
| test_no_overlap_between_supported_and_skipped | 测试支持和跳过的扩展名没有重叠 | 高 |

##### test_config.py

| 测试名称 | 描述 | 优先级 |
|----------|------|--------|
| test_default_config | 测试默认配置 | 高 |
| test_custom_config | 测试自定义配置 | 高 |
| test_is_supported_extension | 测试判断扩展名是否支持 | 高 |
| test_is_excluded_directory | 测试判断目录是否被排除 | 高 |
| test_should_process_file | 测试判断文件是否应该处理 | 高 |
| test_should_process_directory | 测试判断目录是否应该处理 | 高 |
| test_create_download_dir | 测试创建下载目录 | 中 |
| test_download_dir_already_exists | 测试下载目录已存在的情况 | 中 |

---

### 2. 目录遍历测试 (7 个测试)

#### 测试文件
- `tests/test_traversal.py` (7 个测试)

#### 测试用例

| 测试名称 | 描述 | 优先级 | 前置条件 |
|----------|------|--------|----------|
| test_collect_files_empty_directory | 测试空目录 | 高 | 空目录 |
| test_collect_files_with_supported_files | 测试收集支持的文件 | 高 | 包含支持的文件 |
| test_collect_files_with_mixed_files | 测试混合文件类型 | 高 | 包含支持和跳过的文件 |
| test_collect_files_recursive_with_subdirectories | 测试递归遍历子目录 | 高 | 包含子目录 |
| test_collect_files_excludes_directories | 测试排除目录 | 高 | 包含排除目录 |
| test_collect_files_returns_correct_paths | 测试返回正确的文件路径 | 高 | 文件存在 |
| test_get_file_extension | 测试获取文件扩展名 | 高 | 各种文件名 |

#### 测试数据

**空目录测试**:
```
test_dir/
```

**支持的文件测试**:
```
test_dir/
├── test.txt
├── document.pdf
└── spreadsheet.xlsx
```

**混合文件测试**:
```
test_dir/
├── test.txt        # 支持
├── document.pdf    # 支持
├── image.png       # 跳过
└── script.js        # 跳过
```

**递归遍历测试**:
```
test_dir/
├── main.txt
└── subdir/
    └── sub.txt
```

---

### 3. 文件处理测试 (8 个测试)

#### 测试文件
- `tests/test_file_handler.py` (8 个测试)

#### 测试用例

| 测试名称 | 描述 | 优先级 | 前置条件 |
|----------|------|--------|----------|
| test_read_file_content | 测试读取文件内容 | 高 | 文件存在且有内容 |
| test_read_nonexistent_file | 测试读取不存在的文件 | 高 | 文件不存在 |
| test_write_file_content | 测试写入文件内容 | 高 | 目录可写 |
| test_create_directory_structure | 测试创建目录结构 | 高 | 父目录存在 |
| test_reproduce_directory_structure | 测试重建目录结构 | 高 | 源目录结构存在 |
| test_get_relative_path | 测试获取相对路径 | 高 | 两个路径相关 |
| test_is_markdown_file | 测试判断是否为 Markdown 文件 | 中 | 文件路径 |
| test_convert_to_markdown_filename | 测试转换为 Markdown 文件名 | 中 | 文件路径 |

#### 测试数据

**读取文件内容**:
```python
# 输入
test_file.write_text("Hello, World!")

# 预期输出
"Hello, World!"
```

**写入文件内容**:
```python
# 输入
content = "# Markdown Content\n\nThis is a test."
test_file.write_content(test_file, content)

# 预期结果
test_file.read_text() == content
```

---

### 4. 文本转换器测试 (11 个测试)

#### 测试文件
- `tests/test_text_converter.py` (11 个测试)

#### 测试用例

| 测试名称 | 描述 | 优先级 | 输入文件 |
|----------|------|--------|----------|
| test_convert_txt_to_markdown | 测试转换 .txt 文件 | 高 | 包含文本的 .txt 文件 |
| test_convert_md_to_markdown | 测试转换 .md 文件（已经是 Markdown） | 高 | Markdown 文件 |
| test_convert_rst_to_markdown | 测试转换 .rst 文件 | 高 | reStructuredText 文件 |
| test_convert_empty_file | 测试转换空文件 | 中 | 空文本文件 |
| test_convert_large_file | 测试转换大文件 | 中 | 大文本文件 |
| test_convert_file_with_special_characters | 测试转换包含特殊字符的文件 | 中 | 包含特殊字符的文件 |
| test_supports_txt | 测试是否支持 .txt 文件 | 高 | .txt 扩展名 |
| test_supports_md | 测试是否支持 .md 文件 | 高 | .md 扩展名 |
| test_supports_rst | 测试是否支持 .rst 文件 | 高 | .rst 扩展名 |
| test_supports_adoc | 测试是否支持 .adoc 文件 | 高 | .adoc 扩展名 |
| test_does_not_support_other_formats | 测试不支持其他格式 | 中 | 其他扩展名 |

#### 测试数据

**.txt 文件转换**:
```python
# 输入文件
test.txt 内容: "Hello, World!\n\nThis is a test file."

# 预期输出
# 原始文件: test.txt
---
Hello, World!

This is a test file.
```

---

### 5. Word 转换器测试 (13 个测试)

#### 测试文件
- `tests/test_docx_converter.py` (13 个测试)

#### 测试用例

| 测试名称 | 描述 | 优先级 | 输入条件 |
|----------|------|--------|----------|
| test_supports_docx | 测试是否支持 .docx 文件 | 高 | .docx 扩展名 |
| test_supports_doc | 测试是否支持 .doc 文件 | 高 | .doc 扩展名 |
| test_supports_case_insensitive | 测试扩展名大小写不敏感 | 中 | 各种大小写 |
| test_does_not_support_other_formats | 测试不支持其他格式 | 中 | 其他扩展名 |
| test_convert_docx_to_markdown | 测试转换 .docx 文件 | 高 | 有效 .docx 文件 |
| test_convert_empty_document | 测试转换空文档 | 中 | 空 .docx 文档 |
| test_convert_document_with_empty_paragraphs | 测试转换包含空段落的文档 | 中 | 包含空段落 |
| test_convert_document_with_special_characters | 测试转换包含特殊字符的文档 | 中 | 包含特殊字符 |
| test_convert_document_with_multiline_paragraphs | 测试转换包含多行段落的文档 | 中 | 多行段落 |
| test_convert_large_document | 测试转换大文档 | 低 | 大 .docx 文档 |
| test_convert_file_not_found | 测试转换不存在的文件 | 高 | 不存在的文件 |
| test_convert_corrupted_document | 测试转换损坏的文档 | 中 | 损坏的 .docx 文件 |
| test_init | 测试初始化转换器 | 高 | 无 |

---

### 6. PDF 转换器测试 (12 个测试)

#### 测试文件
- `tests/test_pdf_converter.py` (12 个测试)

#### 测试用例

| 测试名称 | 描述 | 优先级 | 输入条件 |
|----------|------|--------|----------|
| test_supports_pdf | 测试是否支持 .pdf 文件 | 高 | .pdf 扩展名 |
| test_supports_case_insensitive | 测试扩展名大小写不敏感 | 中 | 各种大小写 |
| test_does_not_support_other_formats | 测试不支持其他格式 | 中 | 其他扩展名 |
| test_convert_pdf_to_markdown | 测试转换 .pdf 文件 | 高 | 有效 .pdf 文件 |
| test_convert_empty_pdf | 测试转换空 PDF | 中 | 空 .pdf 文件 |
| test_convert_pdf_with_empty_pages | 测试转换包含空页面的 PDF | 中 | 包含空页面 |
| test_convert_pdf_with_special_characters | 测试转换包含特殊字符的 PDF | 中 | 包含特殊字符 |
| test_convert_large_pdf | 测试转换大 PDF | 低 | 大 .pdf 文件 |
| test_convert_file_not_found | 测试转换不存在的文件 | 高 | 不存在的文件 |
| test_convert_corrupted_pdf | 测试转换损坏的 PDF | 中 | 损坏的 .pdf 文件 |
| test_convert_pdf_with_multiline_text_per_page | 测试转换每页多行文本的 PDF | 中 | 多行文本 |
| test_init | 测试初始化转换器 | 高 | 无 |

---

### 7. Excel 转换器测试 (15 个测试)

#### 测试文件
- `tests/test_excel_converter.py` (15 个测试)

#### 测试用例

| 测试名称 | 描述 | 优先级 | 输入条件 |
|----------|------|--------|----------|
| test_supports_xlsx | 测试是否支持 .xlsx 文件 | 高 | .xlsx 扩展名 |
| test_supports_xls | 测试是否支持 .xls 文件 | 高 | .xls 扩展名 |
| test_supports_csv | 测试是否支持 .csv 文件 | 高 | .csv 扩展名 |
| test_supports_case_insensitive | 测试扩展名大小写不敏感 | 中 | 各种大小写 |
| test_does_not_support_other_formats | 测试不支持其他格式 | 中 | 其他扩展名 |
| test_convert_xlsx_to_markdown | 测试转换 .xlsx 文件 | 高 | 有效 .xlsx 文件 |
| test_convert_empty_excel | 测试转换空 Excel | 中 | 空 .xlsx 文件 |
| test_convert_csv_to_markdown | 测试转换 .csv 文件 | 高 | 有效 .csv 文件 |
| test_convert_excel_with_special_characters | 测试转换包含特殊字符的 Excel | 中 | 包含特殊字符 |
| test_convert_large_excel | 测试转换大 Excel | 低 | 大 .xlsx 文件 |
| test_convert_excel_with_multiple_sheets | 测试转换多工作表 Excel | 中 | 多工作表 |
| test_convert_file_not_found | 测试转换不存在的文件 | 高 | 不存在的文件 |
| test_convert_corrupted_excel | 测试转换损坏的 Excel | 中 | 损坏的 .xlsx 文件 |
| test_convert_csv_with_empty_lines | 测试转换包含空行的 CSV | 中 | 包含空行 |
| test_init | 测试初始化转换器 | 高 | 无 |

#### 测试数据

**Excel 转换测试**:
```
输入数据:
| Name  | Age | City    |
|-------|------|----------|
| Alice | 25   | Beijing  |
| Bob   | 30   | Shanghai |

预期输出:
# 原始文件: test.xlsx
---

| Name | Age | City |
|------|-----|--------|
| Alice | 25 | Beijing |
| Bob | 30 | Shanghai |
```

---

### 8. PPT 转换器测试 (13 个测试)

#### 测试文件
- `tests/test_pptx_converter.py` (13 个测试)

#### 测试用例

| 测试名称 | 描述 | 优先级 | 输入条件 |
|----------|------|--------|----------|
| test_supports_pptx | 测试是否支持 .pptx 文件 | 高 | .pptx 扩展名 |
| test_supports_ppt | 测试是否支持 .ppt 文件 | 高 | .ppt 扩展名 |
| test_supports_case_insensitive | 测试扩展名大小写不敏感 | 中 | 各种大小写 |
| test_does_not_support_other_formats | 测试不支持其他格式 | 中 | 其他扩展名 |
| test_convert_pptx_to_markdown | 测试转换 .pptx 文件 | 高 | 有效 .pptx 文件 |
| test_convert_empty_presentation | 测试转换空演示文稿 | 中 | 空 .pptx 文件 |
| test_convert_presentation_with_empty_slides | 测试转换包含空幻灯片的演示文稿 | 中 | 包含空幻灯片 |
| test_convert_presentation_with_special_characters | 测试转换包含特殊字符的演示文稿 | 中 | 包含特殊字符 |
| test_convert_large_presentation | 测试转换大演示文稿 | 低 | 大 .pptx 文件 |
| test_convert_presentation_with_with_multiple_shapes_per_slide | 测试转换每页多个形状的演示文稿 | 中 | 多形状 |
| test_convert_file_not_found | 测试转换不存在的文件 | 高 | 不存在的文件 |
| test_convert_corrupted_presentation | 测试转换损坏的演示文稿 | 中 | 损坏的 .pptx 文件 |
| test_init | 测试初始化转换器 | 高 | 无 |

---

### 9. 转换器注册表测试 (19 个测试)

#### 测试文件
- `tests/test_converter.py` (19 个测试)

#### 测试用例

##### ConverterRegistry 测试

| 测试名称 | 描述 | 优先级 |
|----------|------|--------|
| test_register_converter | 测试注册转换器 | 高 |
| test_register_multiple_converters | 测试注册多个转换器 | 高 |
| test_get_converter_for_txt | 测试获取 TXT 转换器 | 高 |
| test_get_converter_for_docx | 测试获取 DOCX 转换器 | 高 |
| test_get_converter_for_pdf | 测试获取 PDF 转换器 | 高 |
| test_get_converter_for_unsupported_format | 测试获取不支持格式的转换器 | 中 |
| test_case_insensitive_extension | 测试扩展名大小写不敏感 | 中 |

##### get_converter 全局函数测试

| 测试名称 | 描述 | 优先级 | 输入 |
|----------|------|--------|------|
| test_get_converter_for_txt | 测试获取 TXT 转换器 | 高 | test.txt |
| test_get_converter_for_docx | 测试获取 DOCX 转换器 | 高 | test.docx |
| test_get_converter_for_doc | 测试获取 DOC 转换器 | 高 | test.doc |
| test_get_converter_for_pdf | 测试获取 PDF 转换器 | 高 | test.pdf |
| test_get_converter_for_xlsx | 测试获取 XLSX 转换器 | 高 | test.xlsx |
| test_get_converter_for_xls | 测试获取 XLS 转换器 | 高 | test.xls |
| test_get_converter_for_csv | 测试获取 CSV 转换器 | 高 | test.csv |
| test_get_converter_for_pptx | 测试获取 PPTX 转换器 | 高 | test.pptx |
| test_get_converter_for_ppt | 测试获取 PPT 转换器 | 高 | test.ppt |
| test_get_converter_for_unsupported_format | 测试获取不支持格式的转换器 | 中 | test.xyz |
| test_get_converter_for_image | 测试获取图片格式转换器 | 中 | test.png |
| test_get_converter_for_code | 测试获取代码格式转换器 | 中 | test.py |

---

### 10. UI 模块测试 (16 个测试)

#### 测试文件
- `tests/test_progress.py` (8 个测试)
- `tests/test_cli.py` (8 个测试)

#### ProgressTracker 测试用例

| 测试名称 | 描述 | 优先级 |
|----------|------|--------|
| test_initialization | 测试初始化 | 高 |
| test_increment_processed | 测试增加已处理数量 | 高 |
| test_increment_success | 测试增加成功数量 | 高 |
| test_increment_failed | 测试增加失败数量 | 高 |
| test_increment_skipped | 测试增加跳过数量 | 高 |
| test_get_percentage | 测试获取进度百分比 | 高 |
| test_get_percentage_zero_total | 测试总数为零时的百分比 | 中 |
| test_is_complete | 测试是否完成 | 高 |
| test_get_summary | 测试获取摘要 | 高 |

#### CLI 测试用例

| 测试名称 | 描述 | 优先级 |
|----------|------|--------|
| test_initialization | 测试初始化 | 高 |
| test_set_source_dir | 测试设置源目录 | 高 |
| test_set_target_dir | 测试设置目标目录 | 高 |
| test_validate_source_dir_not_set | 测试验证未设置源目录 | 高 |
| test_display_welcome | 测试显示欢迎信息 | 中 |
| test_display_progress | 测试显示进度 | 中 |
| test_display_summary | 测试显示摘要 | 中 |

---

### 11. 主控制器测试 (6 个测试)

#### 测试文件
- `tests/test_main.py` (6 个测试)

#### 测试用例

| 测试名称 | 描述 | 优先级 | 前置条件 |
|----------|------|--------|----------|
| test_initialization | 测试初始化 | 高 | 源目录存在 |
| test_set_target_dir | 测试设置目标目录 | 高 | 有效的目录路径 |
| test_run_without_target_dir | 测试没有设置目标目录时运行 | 高 | 源目录存在 |
| test_run_with_files | 测试运行转换 | 高 | 源目录包含支持的文件 |
| test_run_with_subdirectories | 测试运行转换包含子目录 | 高 | 源目录包含子目录 |
| test_run_with_mixed_files | 测试运行转换混合文件类型 | 高 | 包含支持和跳过的文件 |

#### 测试场景

**场景 1: 基本文件转换**
```
输入:
source_dir/
└── test.txt

预期输出:
output_dir/
└── test.md (转换后的 Markdown 文件)
```

**场景 2: 子目录转换**
```
输入:
source_dir/
├── main.txt
└── subdir/
    └── sub.txt

预期输出:
output_dir/
├── main.md
└── subdir/
    └── sub.md
```

**场景 3: 混合文件类型**
```
输入:
source_dir/
├── test.txt    # 转换
└── image.png   # 跳过

预期输出:
output_dir/
└── test.md      # 只有转换的文件
```

---

### 12. 工具模块测试 (12 个测试)

#### 测试文件
- `tests/test_logger.py` (5 个测试)
- `tests/test_exceptions.py` (7 个测试)

#### Logger 测试用例

| 测试名称 | 描述 | 优先级 |
|----------|------|--------|
| test_initialization | 测试初始化 | 高 |
| test_info | 测试信息日志 | 高 |
| test_warning | 测试警告日志 | 高 |
| test_error | 测试错误日志 | 高 |
| test_multiple_logs | 测试多条日志 | 中 |

#### Exceptions 测试用例

| 测试名称 | 描述 | 优先级 |
|----------|------|--------|
| test_initialization | 测试初始化转换错误 | 高 |
| test_with_file_path | 测试带文件路径的转换错误 | 中 |
| test_initialization | 测试初始化文件未找到错误 | 高 |
| test_is_conversion_error | 测试是否是转换错误 | 高 |
| test_initialization | 测试初始化不支持格式错误 | 高 |
| test_with_file_format | 测试带文件格式的不支持错误 | 中 |
| test_is_conversion_error | 测试是否是转换错误 | 高 |

---

## 测试优先级说明

| 优先级 | 说明 | 执行顺序 |
|--------|------|----------|
| 高 | 核心功能，必须测试 | 先执行 |
| 中 | 重要功能，应该测试 | 次执行 |
| 低 | 辅助功能，可选测试 | 后执行 |

---

## 测试覆盖率目标

| 模块 | 目标覆盖率 | 实际覆盖率 | 状态 |
|--------|-------------|-------------|------|
| config | 100% | 100% | ✅ |
| core | 100% | 100% | ✅ |
| converters | 100% | 100% | ✅ |
| ui | 80% | 90%+ | ✅ |
| utils | 100% | 100% | ✅ |
| main | 80% | 78% | ⚠️ |
| **总体** | **80%** | **93%** | ✅ |

---

## 运行测试

### 运行所有测试
```bash
uv run pytest tests/ -v
```

### 运行特定测试文件
```bash
uv run pytest tests/test_config.py -v
```

### 运行特定测试类
```bash
uv run pytest tests/test_config.py::TestConfig -v
```

### 运行特定测试方法
```bash
uv run pytest tests/test_config.py::TestConfig::test_default_config -v
```

### 运行并显示覆盖率
```bash
uv run pytest tests/ --cov=src --cov-report=term-missing
```

### 生成 HTML 覆盖率报告
```bash
uv run pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html
```

---

## 持续集成建议

### GitHub Actions 配置示例

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"
    - name: Install uv
      run: pip install uv
    - name: Install dependencies
      run: uv sync
    - name: Run tests
      run: uv run pytest tests/ --cov=src --cov-report=xml
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

---

## 测试维护建议

### 添加新功能时

1. 先编写失败的测试（RED 阶段）
2. 实现代码使测试通过（GREEN 阶段）
3. 确保测试覆盖率不低于 80%
4. 添加边界情况测试

### 重构代码时

1. 确保所有现有测试通过
2. 不要删除测试
3. 添加新的测试用例以覆盖重构的代码

### 修复 Bug 时

1. 先编写重现 Bug 的测试
2. 修复 Bug
3. 确保测试通过
4. 添加回归测试防止类似问题

---

*文档生成时间: 2026-02-22*
