from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse

from app.models.schemas import FileListResponse, UploadResponse, DeleteResponse, ClearAllResponse
from app.services.file_service import file_service

router = APIRouter()


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
