# 贡献指南

感谢你考虑为 FileShare 做出贡献！

## 🤝 如何贡献

我们欢迎各种形式的贡献，包括但不限于：

- 🐛 报告 Bug
- 💡 提出新功能建议
- 📝 改进文档
- 🔧 提交代码修复
- ✨ 开发新功能

## 📋 贡献流程

### 1. Fork 仓库

点击 GitHub 仓库右上角的 "Fork" 按钮，将仓库 Fork 到你的账号下。

### 2. 克隆仓库

```bash
git clone https://github.com/sylvie-233/FileShare.git
cd FileShare
```

### 3. 创建分支

为你的贡献创建一个新的分支：

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-bug-fix
```

### 4. 进行更改

- 遵循现有的代码风格
- 添加必要的注释
- 确保代码通过测试（如果有）
- 更新相关文档

### 5. 提交更改

```bash
git add .
git commit -m "描述你的更改"
```

提交信息应该清晰描述你的更改，例如：
- `feat: 添加文件预览功能`
- `fix: 修复移动端链接显示问题`
- `docs: 更新 README 安装说明`

### 6. 推送到你的 Fork

```bash
git push origin feature/your-feature-name
```

### 7. 创建 Pull Request

- 访问你 Fork 的仓库
- 点击 "New Pull Request"
- 填写 PR 描述，说明你的更改
- 等待代码审查

## 📝 代码规范

### Python 代码

项目使用 Ruff 进行代码检查和格式化：

```bash
# 检查代码
uv run ruff check app/

# 格式化代码
uv run ruff format app/

# 同时检查和格式化
uv run ruff check --fix app/
uv run ruff format app/
```

- 使用有意义的变量和函数名
- 添加类型提示
- 编写文档字符串
- 遵循 Ruff 配置的代码风格

### JavaScript 代码

- 使用现代 ES6+ 语法
- 保持函数简洁
- 添加必要的注释

### Git 提交信息

使用语义化的提交信息：

- `feat:` 新功能
- `fix:` Bug 修复
- `docs:` 文档更新
- `style:` 代码格式（不影响代码运行）
- `refactor:` 重构（既不是新功能也不是修复）
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

## 🐛 报告 Bug

在报告 Bug 之前，请先搜索 Issues，确认问题未被报告。

报告 Bug 时请包含：

1. **问题描述** - 清晰描述遇到的问题
2. **复现步骤** - 详细说明如何复现问题
3. **预期行为** - 描述你期望发生什么
4. **实际行为** - 描述实际发生了什么
5. **环境信息**：
   - 操作系统
   - Python 版本
   - 浏览器版本（如果是前端问题）
6. **截图** - 如果适用，提供截图

## 💡 功能建议

我们欢迎功能建议！在提出建议前，请考虑：

- 这个功能是否适合这个项目？
- 是否有类似的功能已经存在？
- 描述清楚这个功能的用途和价值

## 📧 联系方式

如果你有任何问题，可以通过以下方式联系：

- GitHub Issues: [https://github.com/sylvie-233/FileShare/issues](https://github.com/sylvie-233/FileShare/issues)

## 📄 行为准则

- 尊重所有贡献者
- 接受建设性批评
- 专注于对社区最有利的事情
- 对其他社区成员表示同理心

感谢你的贡献！🎉
