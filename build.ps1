# FileShare 打包工具

# 检查 PowerShell 版本
if ($PSVersionTable.PSVersion.Major -lt 7) {
    Write-Host "[错误] 本脚本需要 PowerShell 7.0 或更高版本" -ForegroundColor Red
    Write-Host "当前版本: $($PSVersionTable.PSVersion)" -ForegroundColor Yellow
    Write-Host "请升级 PowerShell 或使用 PowerShell 7+ 运行本脚本" -ForegroundColor Yellow
    Read-Host "按任意键退出"
    exit 1
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   FileShare 打包工具" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# [1/2] 检查环境并安装依赖
Write-Host "[1/2] 检查环境并安装依赖..." -ForegroundColor Yellow
if (-not (Test-Path ".venv")) {
    Write-Host "[错误] 虚拟环境不存在，请先运行: uv sync" -ForegroundColor Red
    Read-Host "按任意键退出"
    exit 1
}

$env:VIRTUAL_ENV = Join-Path (Get-Location) ".venv"
$env:PATH = "$env:VIRTUAL_ENV\Scripts;$env:PATH"

uv add --dev pyinstaller

# [2/2] 开始打包
Write-Host "[2/2] 开始打包..." -ForegroundColor Yellow

# 使用数组来避免 PowerShell 解析问题
$pyinstallerArgs = @(
    'run.py',
    '--name=FileShare',
    '--onefile',
    '--console',  # 使用控制台模式
    '--clean',
    '--icon', 'resources/favicon.ico',
    '--add-data', 'static;static',
    '--add-data', 'app;app',
    '--add-data', 'resources;resources',
    '--hidden-import', 'fastapi',
    '--hidden-import', 'fastapi.middleware.cors',
    '--hidden-import', 'fastapi.responses',
    '--hidden-import', 'fastapi.staticfiles',
    '--hidden-import', 'pydantic',
    '--hidden-import', 'pydantic_settings',
    '--hidden-import', 'uvicorn',
    '--hidden-import', 'uvicorn.lifespan',
    '--hidden-import', 'uvicorn.protocols',
    '--hidden-import', 'uvicorn.server',
    '--hidden-import', 'uvicorn.supervisors',
    '--hidden-import', 'uvicorn.workers'
)

uv run pyinstaller @pyinstallerArgs

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "[错误] 打包失败！" -ForegroundColor Red
    Read-Host "按任意键退出"
    exit 1
}

Write-Host ""
Write-Host "[成功] 打包完成！" -ForegroundColor Green
Write-Host ""
Write-Host "可执行文件位置: dist\FileShare.exe" -ForegroundColor Cyan
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Read-Host "按任意键退出"
