import os
import shutil
from pathlib import Path
from typing import List
from fastapi import UploadFile, HTTPException

from app.core.config import settings
from app.models.schemas import FileInfo


class FileService:
    def __init__(self):
        self.upload_dir = settings.UPLOAD_DIR

    async def save_file(self, file: UploadFile) -> str:
        file_path = self.upload_dir / file.filename

        if file_path.exists():
            raise HTTPException(status_code=400, detail="文件已存在")

        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            return file.filename
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"文件保存失败: {str(e)}")

    def list_files(self) -> List[FileInfo]:
        files = []
        for file_path in self.upload_dir.iterdir():
            if file_path.is_file():
                stat = file_path.stat()
                files.append(FileInfo(name=file_path.name, size=stat.st_size, modified=stat.st_mtime))
        return files

    def get_file_path(self, filename: str) -> Path:
        file_path = self.upload_dir / filename
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="文件不存在")
        return file_path

    def delete_file(self, filename: str) -> str:
        file_path = self.upload_dir / filename
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="文件不存在")

        try:
            os.remove(file_path)
            return filename
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"文件删除失败: {str(e)}")

    def clear_all_files(self) -> int:
        count = 0
        try:
            for file_path in self.upload_dir.iterdir():
                if file_path.is_file():
                    os.remove(file_path)
                    count += 1
            return count
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"清空文件失败: {str(e)}")


file_service = FileService()
