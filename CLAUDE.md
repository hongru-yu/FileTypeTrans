# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

FileTypeTrans - 使用 uv 管理的 Python 项目

## 开发命令

### 依赖管理
```bash
# 添加依赖
uv add <package-name>

# 添加开发依赖
uv add --dev <package-name>

# 同步依赖
uv sync

# 移除依赖
uv remove <package-name>
```

### 运行代码
```bash
# 运行主程序
uv run main.py

# 运行 Python 脚本
uv run python <script.py>
```

### 虚拟环境
```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate
```

## 项目配置

- 包管理工具: uv
- Python 版本要求: >= 3.10
- 项目配置文件: pyproject.toml
- 主入口文件: main.py
