# 📁 FileShare

一个基于 FastAPI 的局域网文件共享服务，支持拖拽上传、文件管理、移动端适配等功能。

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ 功能特性

- 📤 **拖拽上传** - 支持拖拽文件到指定区域上传
- 📱 **移动端适配** - 响应式设计，完美适配手机和平板
- 🔗 **分享链接** - 一键复制分享链接，方便局域网内访问
- 📂 **文件管理** - 上传、下载、删除文件
- 🗑️ **一键清空** - 快速清空所有上传的文件
- 🎨 **现代化UI** - 美观的渐变背景和流畅的动画效果
- 📊 **文件信息** - 显示文件大小和修改时间
- 🔔 **实时通知** - 操作成功/失败的即时反馈
- ⚡ **高性能** - 基于 FastAPI 和 Uvicorn，快速响应

## 🛠️ 技术栈

- **后端框架**: FastAPI 0.115+
- **ASGI 服务器**: Uvicorn
- **数据验证**: Pydantic
- **代码检查**: Ruff
- **测试框架**: pytest
- **前端**: 原生 HTML/CSS/JavaScript
- **包管理**: uv

## 📦 安装

### 前置要求

- Python 3.13+
- uv

### 安装步骤

```bash
# 克隆项目
git clone https://github.com/sylvie-233/FileShare.git
cd FileShare

# 使用 uv 安装依赖
uv sync

# 复制环境变量配置文件
cp .env.example .env
```

## 🚀 快速开始

### 启动服务

```bash
# 使用 uv
uv run python run.py

# 或使用虚拟环境
python run.py
```

服务将在 `http://0.0.0.0:8000` 启动。

### 访问应用

- 本地访问: `http://localhost:8000`
- 局域网访问: `http://你的IP:8000` (例如: `http://192.168.1.100:8000`)

## 📖 使用说明

### 上传文件

1. 将文件拖拽到上传区域
2. 或点击上传区域选择文件
3. 等待上传完成

### 管理文件

- **下载文件**: 点击文件列表中的"下载"按钮
- **删除文件**: 点击文件列表中的"删除"按钮
- **清空全部**: 点击"清空全部"按钮，确认后删除所有文件

### 分享链接

1. 页面顶部显示当前访问链接
2. 点击"复制链接"按钮
3. 将链接分享给局域网内的其他用户

## 📁 项目结构

```
FileShare/
├── app/                      # 应用主包
│   ├── __init__.py
│   ├── main.py               # FastAPI 应用入口
│   ├── api/                  # API 路由层
│   │   ├── __init__.py
│   │   └── files.py          # 文件相关 API
│   ├── core/                 # 核心配置
│   │   ├── __init__.py
│   │   └── config.py         # 应用配置
│   ├── models/               # 数据模型
│   │   ├── __init__.py
│   │   └── schemas.py       # Pydantic 模型
│   └── services/             # 业务逻辑层
│       ├── __init__.py
│       └── file_service.py   # 文件服务
├── static/                   # 静态文件
│   └── index.html           # 前端页面
├── tests/                   # 测试目录
│   └── __init__.py
├── uploads/                 # 上传文件存储目录
├── .env.example            # 环境变量示例
├── .gitignore             # Git 忽略文件
├── .python-version        # Python 版本
├── pyproject.toml        # 项目配置
├── run.py               # 运行脚本
└── README.md            # 项目说明
```

## 🔌 API 文档

启动服务后访问交互式 API 文档:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## ⚙️ 配置说明

在 `.env` 文件中配置以下参数:

```env
PROJECT_NAME=FileShare
VERSION=0.1.0
API_V1_PREFIX=/api/v1

HOST=0.0.0.0
PORT=8000

UPLOAD_DIR=uploads
MAX_FILE_SIZE=104857600  # 100MB
```

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤:

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

项目使用 Ruff 进行代码检查和格式化：

```bash
# 安装开发依赖
uv sync --all-extras

# 检查代码
uv run ruff check app/

# 格式化代码
uv run ruff format app/

# 同时检查和格式化
uv run ruff check --fix app/
uv run ruff format app/
```

详细的贡献指南请查看 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 运行测试

项目使用 pytest 进行测试：

```bash
# 安装开发依赖
uv sync --all-extras

# 运行测试
uv run pytest tests/ -v

# 运行特定测试文件
uv run pytest tests/test_file_service.py -v

# 运行测试并生成覆盖率报告
uv run pytest tests/ --cov=app --cov-report=html
```

## 📝 开发计划

- [ ] 文件夹管理
- [ ] 文件重命名
- [ ] 文件预览功能
- [ ] 批量操作
- [ ] 文件搜索
- [ ] 用户认证
- [ ] 权限管理
- [ ] 文件分享链接有效期
- [ ] 上传进度显示
- [ ] 断点续传

## 🐛 常见问题

### Q: 上传文件失败怎么办？

A: 请检查文件大小是否超过限制（默认 100MB），检查上传目录权限。

### Q: 局域网内其他设备无法访问？

A: 请确保防火墙允许 8000 端口，检查设备是否在同一局域网。

### Q: 如何修改上传文件大小限制？

A: 在 `.env` 文件中修改 `MAX_FILE_SIZE` 参数。

### Q: 如何修改服务端口？

A: 在 `.env` 文件中修改 `PORT` 参数。

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- [FastAPI](https://fastapi.tiangolo.com/) - 现代化的 Python Web 框架
- [Uvicorn](https://www.uvicorn.org/) - 快速的 ASGI 服务器
- [Pydantic](https://docs.pydantic.dev/) - 数据验证库

## 📮 联系方式

- 项目主页: [https://github.com/sylvie-233/FileShare](https://github.com/sylvie-233/FileShare)
- 问题反馈: [https://github.com/sylvie-233/FileShare/issues](https://github.com/sylvie-233/FileShare/issues)

---

如果这个项目对你有帮助，请给个 ⭐️ Star 支持一下！
