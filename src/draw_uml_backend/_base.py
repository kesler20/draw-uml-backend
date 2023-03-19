from dataclasses import dataclass
from pathlib import Path
from draw_uml_backend.file import File
from draw_uml_backend.source_code import SourceCode

BASE_OUTPUT_RESPONSE_PATH = "output"

@dataclass
class BaseReader:
    response_code_path: str

    @property
    def source(self):
        return SourceCode(self.response_code_path)

    def clean_up(sef, file_to_remove: str):
        print("================== next =")
        print(file_to_remove)

    def append(self, filename: str, content: str):
        File(Path(filename)).append(content)

    def write(self, filename: str, content: str):
        File(Path(filename)).write(content)