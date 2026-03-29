import socket

from fastapi import APIRouter, File, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse

from app.core.config import settings
from app.core.logger import get_logger
from app.models.schemas import ClearAllResponse, DeleteResponse, FileListResponse, UploadResponse
from app.services.file_service import file_service

# 获取日志记录器
logger = get_logger(__name__)

router = APIRouter()


def get_local_ip():
    """获取本机的实际IP地址"""
    try:
        # 创建一个UDP socket连接到外部地址，获取本地IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        # 如果获取失败，返回localhost
        return "localhost"


@router.get("/server-info")
async def get_server_info(request: Request):
    """获取服务器信息，包括实际IP地址"""
    # 获取本机实际IP地址
    local_ip = get_local_ip()
    host = f"{local_ip}:{settings.PORT}"

    scheme = request.url.scheme
    server_url = f"{scheme}://{host}"
    return {"server_url": server_url}


@router.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    try:
        logger.info(f"上传文件: {file.filename}")
        filename = await file_service.save_file(file)
        logger.info(f"文件上传成功: {filename}")
        return UploadResponse(filename=filename, status="success")
    except HTTPException as e:
        logger.error(f"文件上传失败: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"文件上传异常: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/files", response_model=FileListResponse)
async def list_files():
    logger.info("获取文件列表")
    files = file_service.list_files()
    logger.info(f"获取到 {len(files)} 个文件")
    return FileListResponse(files=files)


@router.get("/download/{filename}")
async def download_file(filename: str):
    logger.info(f"下载文件: {filename}")
    try:
        file_path = file_service.get_file_path(filename)
        logger.info(f"文件下载成功: {filename}")
        return FileResponse(file_path, filename=filename)
    except HTTPException as e:
        logger.error(f"文件下载失败: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"文件下载异常: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/files/{filename}", response_model=DeleteResponse)
async def delete_file(filename: str):
    try:
        logger.info(f"删除文件: {filename}")
        deleted_filename = file_service.delete_file(filename)
        logger.info(f"文件删除成功: {deleted_filename}")
        return DeleteResponse(status="success", filename=deleted_filename)
    except HTTPException as e:
        logger.error(f"文件删除失败: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"文件删除异常: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/files", response_model=ClearAllResponse)
async def clear_all_files():
    try:
        logger.info("清空所有文件")
        count = file_service.clear_all_files()
        logger.info(f"清空成功，删除了 {count} 个文件")
        return ClearAllResponse(status="success", count=count)
    except HTTPException as e:
        logger.error(f"清空文件失败: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"清空文件异常: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
