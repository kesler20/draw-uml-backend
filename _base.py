import os
from dataclasses import dataclass
from read_only.source_code import SourceCode
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
