from draw_uml_backend.file import File
import os
from dataclasses import dataclass
from draw_uml_backend.source_code import SourceCode
from pathlib import Path


@dataclass
class BaseReader:
    response_code_path: str

    @property
    def source(self):
        return SourceCode(self.response_code_path)

    def clean_up(sef, file_to_remove: str):
        if Path(file_to_remove).exists():
            os.remove(file_to_remove)
        
    def append(self, filename: str,content: str):
        File(Path(filename)).append(content)

    def write(self, filename: str,content: str):
        File(Path(filename)).write(content)