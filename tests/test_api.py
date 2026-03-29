import tempfile
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.file_service import file_service


class TestAPI:
    def setup_method(self):
        # Create a temporary directory for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_upload_dir = file_service.upload_dir
        file_service.upload_dir = Path(self.temp_dir.name)
        self.client = TestClient(app)
    
    def teardown_method(self):
        # Restore original upload directory
        file_service.upload_dir = self.original_upload_dir
        self.temp_dir.cleanup()
    
    def test_get_files_empty(self):
        """Test getting files when no files are uploaded"""
        response = self.client.get("/api/v1/files")
        assert response.status_code == 200
        assert response.json() == {"files": []}
    
    def test_clear_all_files(self):
        """Test clearing all files"""
        response = self.client.delete("/api/v1/files")
        assert response.status_code == 200
        assert "status" in response.json()
        assert "count" in response.json()
