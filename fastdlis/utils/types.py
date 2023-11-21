from typing import TypeVar, TypedDict
from pathlib import Path

from dlisio.dlis import PhysicalFile

InputFile = TypeVar('InputFile', PhysicalFile, str, Path)


class DlisFileDict(TypedDict):
    """
    A dictionary containing basic information about a .dlis file.
    """
    file: str
    well: str
    size: str
    error: bool
    error_message: str
    logical_files: int
