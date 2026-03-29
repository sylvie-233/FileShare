import os
import tempfile
from pathlib import Path
from app.services.file_service import file_service
from fastapi import HTTPException


class TestFileService:
    def setup_method(self):
        # Create a temporary directory for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_upload_dir = file_service.upload_dir
        file_service.upload_dir = Path(self.temp_dir.name)
    
    def teardown_method(self):
        # Restore original upload directory
        file_service.upload_dir = self.original_upload_dir
        self.temp_dir.cleanup()
    
    def test_list_files_empty(self):
        """Test listing files when directory is empty"""
        files = file_service.list_files()
        assert len(files) == 0
    
    def test_delete_nonexistent_file(self):
        """Test deleting a nonexistent file"""
        try:
            file_service.delete_file("nonexistent.txt")
            assert False, "Should have raised HTTPException"
        except HTTPException as e:
            assert e.status_code == 404
            assert "文件不存在" in e.detail
    
    def test_clear_all_files(self):
        """Test clearing all files"""
        # Create test files
        (file_service.upload_dir / "test1.txt").write_text("test1")
        (file_service.upload_dir / "test2.txt").write_text("test2")
        
        # Clear all files
        count = file_service.clear_all_files()
        assert count == 2
        
        # Verify directory is empty
        files = file_service.list_files()
        assert len(files) == 0
