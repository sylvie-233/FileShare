import logging
from logging.handlers import TimedRotatingFileHandler

from app.core.paths import get_exe_dir

# 创建日志目录
LOGS_DIR = get_exe_dir() / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# 配置根日志记录器
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)

# 文件处理器（按日期滚动）
file_handler = TimedRotatingFileHandler(
    filename=str(LOGS_DIR / "app.log"),
    when="midnight",  # 每天午夜滚动
    interval=1,  # 每天滚动一次
    backupCount=7,  # 保留7天的日志
    encoding="utf-8",
)
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# 添加处理器到根日志记录器
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


# 创建应用特定的日志记录器
def get_logger(name: str = "app") -> logging.Logger:
    """获取指定名称的日志记录器"""
    return logging.getLogger(name)
