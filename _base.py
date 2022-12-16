from dataclasses import dataclass
from read_only.source_code import SourceCode


@dataclass
class BaseReader:
    response_code_path: str

    @property
    def source(self):
        return SourceCode(self.response_code_path)
