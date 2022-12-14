from typing import Protocol, List, Iterable, Tuple, Any, Optional, Union


class DataFrameLocator(Protocol):
    loc: Union[List[List[Any]], List[Any]]

    def __getitem__(self, other: Any, another: Any = None):
        ...

    def __setitem__(self, item: Any, anotherItem: Any = None) -> Any:
        ...

class DataFrame(Protocol):

    def __getitem__(self, other: Any, another: Any = None) -> DataFrameLocator:
        ...

    def __setitem__(self, item: Any, anotherItem: Any = None) -> Any:
        ...

    @property
    def at(self) -> DataFrameLocator:
        ...

    @property
    def iat(self) -> DataFrameLocator:
        ...

    @property
    def loc(self) -> DataFrameLocator:
        ...

    @property
    def columns(self) -> Iterable[Any]:
        ...

    @property
    def index(self) -> Iterable[Any]:
        ...

    @property
    def count(self) -> Tuple[Any]:
        ...

    @property
    def shape(self) -> Tuple[Any]:
        ...

    @property
    def axes(self) -> Tuple[Any]:
        ...

    @property
    def values(self) -> List[List[Any]]:
        ...

    @property
    def info(self) -> None:
        ...

    def head(self, n: int) -> Any:
        ...

    def tail(self, n: int) -> Any:
        ...

    def to_excel(self, filename: str, sheet_name: str, index: Optional[bool] = False) -> None:
        ...

    def drop(self, axes: List[Any], inplace: Optional[bool]) -> None:
        ...

    def insert(self, column_index: int, column_name: str, column_values: List[Any]) -> None:
        ...

    def pop(self, column_name: str) -> None:
        ...
    
    def sample(self,n: int) -> Any:
        ...
