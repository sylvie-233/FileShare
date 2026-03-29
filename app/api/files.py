import socket

from fastapi import APIRouter, File, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse

from app.core.config import settings
from app.models.schemas import ClearAllResponse, DeleteResponse, FileListResponse, UploadResponse
from app.services.file_service import file_service

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
        filename = await file_service.save_file(file)
        return UploadResponse(filename=filename, status="success")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/files", response_model=FileListResponse)
async def list_files():
    files = file_service.list_files()
    return FileListResponse(files=files)


@router.get("/download/{filename}")
async def download_file(filename: str):
    file_path = file_service.get_file_path(filename)
    return FileResponse(file_path, filename=filename)


@router.delete("/files/{filename}", response_model=DeleteResponse)
async def delete_file(filename: str):
    try:
        deleted_filename = file_service.delete_file(filename)
        return DeleteResponse(status="success", filename=deleted_filename)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/files", response_model=ClearAllResponse)
async def clear_all_files():
    try:
        count = file_service.clear_all_files()
        return ClearAllResponse(status="success", count=count)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
