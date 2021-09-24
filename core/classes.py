import base64
import os
from datetime import datetime
from typing import Optional

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from csedu_research_hub.settings import MEDIA_ROOT


class OverwriteFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name: str, max_length: Optional[int]):
        if self.exists(name):
            self.delete(name)
        return name


class FileManager:
    def __init__(self):
        self.storage_system = OverwriteFileSystemStorage()

    def save_file(self, file: any, mimetype: str, folder_path: str):
        now = datetime.now()
        instance_file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + f".{mimetype}"
        filename = os.path.join(MEDIA_ROOT, folder_path, instance_file_name)
        self.storage_system.save(filename, file)
        return filename

    def delete_file(self, path: str):
        self.storage_system.delete(path)
