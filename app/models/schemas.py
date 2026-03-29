from typing import List

from pydantic import BaseModel


class FileInfo(BaseModel):
    name: str
    size: int
    modified: float


class FileListResponse(BaseModel):
    files: List[FileInfo]


class UploadResponse(BaseModel):
    filename: str
    status: str


class DeleteResponse(BaseModel):
    status: str
    filename: str


class ClearAllResponse(BaseModel):
    status: str
    count: int
