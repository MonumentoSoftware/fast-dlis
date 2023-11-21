import os
import pathlib
from typing import Tuple, List
from collections import Counter
from .searcher import Searcher

FileTag = Tuple[str, pathlib.Path]


def find_duplicate_tags(file_tags: List[FileTag]) -> List[FileTag]:
    tag_count = Counter(tag for tag, _ in file_tags)
    return [tag for tag in file_tags if tag_count[tag[0]] > 1]


def get_folders(path: str) -> List[pathlib.Path]:
    """
    Get all folders inside the given path.

    Args:
        path (str): A string describing the path

    Returns:
        List[pathlib.Path]: A list of folder paths in the parent path
    """
    root_directory = pathlib.Path(path)
    return [folder for folder in root_directory.iterdir() if folder.is_dir()]


def get_files(path: str) -> List[pathlib.Path]:
    """
    Get all files inside the given path.

    Args:
        path (str): A string describing the path

    Returns:
        List[pathlib.Path]: A list of file paths in the parent path
    """
    root_directory = pathlib.Path(path)
    return [file for file in root_directory.iterdir() if file.is_file()]


def get_file_tags(dir_path: str, extensions: List[str]) -> List[FileTag]:
    """
    Gets all files in a directory with specified extensions,
    creating file tags.

    Args:
        dir_path (str): A path to the directory to be scanned
        extensions (List[str]): A list of strings representing the extensions

    Returns:
        List[FileTag]: A list (folder name, file path), sorted by file size
    """
    assert isinstance(dir_path, str), 'Please provide a path string'
    assert isinstance(extensions, list), 'Please provide a list of strings'

    result_tuples = []
    for folder in get_folders(dir_path):
        files = Searcher.search_extensions(folder, set(extensions))
        result_tuples.extend((folder.name, file) for file in files)

    return sorted(result_tuples, key=lambda x: os.stat(x[1]).st_size)
