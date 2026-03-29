from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.api.files import router as files_router
from app.core.config import settings
from app.core.logger import get_logger
from app.core.paths import get_base_path

# 获取日志记录器
logger = get_logger(__name__)

static_dir = get_base_path() / "static"


def create_app() -> FastAPI:
    logger.info(f"启动 {settings.PROJECT_NAME} v{settings.VERSION}")
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    app.include_router(files_router, prefix=settings.API_V1_PREFIX)

    @app.get("/", response_class=HTMLResponse)
    async def root():
        with open(static_dir / "index.html", "r", encoding="utf-8") as f:
            return f.read()

    return app


app = create_app()
